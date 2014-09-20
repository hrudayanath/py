#bus_monitor.py

#4373 -87.6297836304
#4375 -87.6619300842

import urllib
from xml.etree.ElementTree import parse

candids = ['4373', '4375']
daves_lon = -87.668442 

def distance(lon1, lon2):
  #return distance between the longitudes
  return 69*(lon1 - lon2)

def monitor():
  u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
  doc = parse (u)
  for bus in doc.findall('bus'):
    busid = bus.findtext('id')
    if busid in candids:
       lat = float (bus.findtext('lon'))
       dis = distance(lat,daves_lon)
       print 'busid ::', busid, "dist::", dis, "miles"
  print '-'*10   

import time
while True:
    monitor()
    time.sleep(60) 





