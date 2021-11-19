#!/usr/bin/env python
import sys
for data in sys.stdin:
    data = data.strip()
    date = data[15:23]
    temp = int(data[87:92])
    quality = int(data[92])
    if (temp != 9999):
       if quality == 1 or quality == 0 or quality == 4 or quality == 5 or quality == 9:
          print('%s\t%s' % (date, temp))
        
        
