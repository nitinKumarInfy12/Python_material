#!/usr/bin/env python

import os

for path in ('c:/windows','/etc', '../DATA', '/wombat', '/tmp', 'RESULTS', 'C:/temp'): # <1>
    print(path, end=' ') # <2>
    if os.path.exists(path):  # <3>
        print('exists')
    else:
        print('does not exist')
