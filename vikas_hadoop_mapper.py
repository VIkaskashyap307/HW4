#!/usr/bin/env python
import sys
for data in sys.stdin:
    data = data.strip()
    date = data[15:23]
    temp = data[87:92]
    quality = data[93]
    if temp != "9999" and (data[93] == "1" or data[93] == "0" or data[93] == "4" or data[93] == "5" or data[93] == "9"):
        print('%s\t%s' % (date, temp))
        
        
