#find_north.py
#find all buses travelling the north bound of the dave office

dave_latitude = 41.98062
dave_longitude = -87.668442

from xml.etree.ElementTree import parse
doc = parse ('rt22.xml')

for bus in doc.findall('bus'):
   lat = float(bus.findtext('lon'))
   if  lat > dave_longitude:
     direction = bus.findtext('d')
     if direction.startswith('North'):
        busid = bus.findtext('id')
        print busid, lat
