#!/usr/bin/env python
  
from operator import itemgetter
import sys
  
current_word = None
MIN_INT = -sys.maxsize - 1
word = None

temp_map = {}

for data in sys.stdin:
    data = data.strip()
    date, temp = data.split('\t', 1)
    try:
        temp = int(temp)
    except ValueError:
        continue

    if date not in temp_map:
        temp_map[date] = temp
    else:
        if temp > temp_map[date]:
            temp_map[date] = temp

for item in temp_map:
    print ('%s\t%s' % (item, temp_map[item]))