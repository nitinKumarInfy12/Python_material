#!/usr/bin/env python
import os
from datetime import datetime

def format_time(ts):
    """convert time stamp to YYYY-MM-DD HH:MM string"""
    dt = datetime.fromtimestamp(ts) # <1>
    s = dt.strftime('%Y-%m-%d %H:%M') # <2>

    return s

filenames = ( # <3>
    '../DATA/alice.txt',
    '../ANSWERS/sieve.py',
    'file_attrib.py',
)

for filename in filenames:
    size = os.path.getsize(filename) # <4>
    mtime_ts = os.path.getmtime(filename) # <5>
    mtime = format_time(mtime_ts)

    atime_ts = os.path.getatime(filename) # <6>
    atime = format_time(atime_ts)


    print('{0:20s} {1:8d}  {2}  {3}'.format(filename, size, mtime, atime))
