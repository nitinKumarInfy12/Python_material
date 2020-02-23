#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 13 09:01:14 2013

"""
import os

info = os.stat('../DATA/parrot.txt') # <1>
print(info) # <2>

print('size is', info[6]) # <3>
print('size is', info.st_size) # <4>

