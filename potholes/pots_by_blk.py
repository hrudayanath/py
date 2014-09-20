# pots_by_zip.py
#
# An example of parsing potholes data and tabulating results.
# This program reads the CSV data and tabulates potholes
# according to zip-code.    Use this as a rough code template
# for solving the problem of finding the worst street on
# which to bike.

import csv

def find_blockadd(zipcode , street):
   return street.split(' ',1)[1] +' '+ zipcode

def make_address(addrs):
   parts = addrs.split()
   parts[0] = parts[0][:-3] + 'XXX'
   return ' '.join(parts)

# Dictionary used to tabulate results
potholes_by_straddr = {}

f = open('./potholes.csv', 'r')
for row in csv.DictReader(f):
    status = row['STATUS']
    zipcode = row['ZIP']
    street = row['STREET ADDRESS']
    if status == 'Open':
        blk_add = find_blockadd(zipcode, street)
        if blk_add not in potholes_by_straddr:
            potholes_by_straddr[blk_add] = 1
        else:
            potholes_by_straddr[blk_add] += 1

# Print a table showing the number of open potholes by zipcode
print('Number of open potholes by street and zip')
for key, value in sorted(potholes_by_straddr.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)

'''
for ba in sorted(potholes_by_straddr):
    print('%8s %d' % (ba, potholes_by_straddr[ba]))
'''
