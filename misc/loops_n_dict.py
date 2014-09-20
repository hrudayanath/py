#!/usr/bin/python


lst = ['apple','apple','banana','banana','banana']

cnt = {}

for i in lst:
   if i in cnt:
     cnt[i] += 1
   else:
     cnt[i] = 1

print cnt
