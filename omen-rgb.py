#!/usr/bin/env python3

from time import sleep
from secrets import token_hex
from sys import argv
from random import randint

zone0 = open("/sys/devices/platform/hp-wmi/rgb_zones/zone00","r+")
zone1 = open("/sys/devices/platform/hp-wmi/rgb_zones/zone01","r+")
zone2 = open("/sys/devices/platform/hp-wmi/rgb_zones/zone02","r+")
zone3 = open("/sys/devices/platform/hp-wmi/rgb_zones/zone03","r+")

def gencolor():
  rand=randint(1,3)
  if(rand==1):
    r=255
    g=randint(1,12)*16-1
    b=randint(1,12)*16-1
  elif(rand==2):
    r=randint(1,12)*16-1
    g=255
    b=randint(1,12)*16-1
  else:
    r=randint(1,12)*16-1
    g=randint(1,12)*16-1
    b=255
  
  return "0x"f"{r:02x}{g:02x}{b:02x}"

def parse(zone):
  value=zone.read()
  zone.seek(0)

  r=int(value.replace(",", "").split(" ")[1])
  g=int(value.replace(",", "").split(" ")[3])
  b=int(value.replace(",", "").split(" ")[5])
  return r,g,b

if argv[1] == "disco":
  slp=0.1
  if len(argv) > 2:
    slp=float(argv[2])
  while True:
    zone0.write(gencolor())
    zone0.seek(0)
    zone1.write(gencolor())
    zone1.seek(0)
    zone2.write(gencolor())
    zone2.seek(0)
    zone3.write(gencolor())
    zone3.seek(0)
    sleep(slp)

if argv[1] == "disco0":
  slp=0.1
  if len(argv) > 2:
    slp=float(argv[2])
  while True:
    zone0.write(token_hex(3))
    zone0.seek(0)
    zone1.write(token_hex(3))
    zone1.seek(0)
    zone2.write(token_hex(3))
    zone2.seek(0)
    zone3.write(token_hex(3))
    zone3.seek(0)
    sleep(slp)

if argv[1] == "reset":
  zone0.write("0F84FA")
  zone0.seek(0)
  zone1.write("710FFA")
  zone1.seek(0)
  zone2.write("F9350F")
  zone2.seek(0)
  zone3.write("FAAC0F")
  zone3.seek(0)
