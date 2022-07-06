#!/usr/bin/python3""
"""a script that reads stdin line by line and computes metrics"""

import sys
import re
import random
import datetime
from time import sleep

total_size = 0
lines_by_status = {}

while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            continue
        ip, date, request, status, size = re.split(r'\s+', line)
        total_size += int(size)
        if status in lines_by_status:
            lines_by_status[status] += 1
        else:
            lines_by_status[status] = 1
    except KeyboardInterrupt:
        break

