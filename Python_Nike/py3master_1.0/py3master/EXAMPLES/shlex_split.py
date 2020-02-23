#!/usr/bin/env python
# (c) 2018 CJ Associates
#
import shlex

cmd = 'herp derp "fuzzy bear" "wanga tanga" pop'  # <1>

print(cmd.split())  # <2>
print()

print(shlex.split(cmd))  # <3>
