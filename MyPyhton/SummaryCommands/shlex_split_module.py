Using shlex.split()
• Splits string
• Preserves white space

If you have an external command you want to execute, you should split it into individual words.
If your command has quoted whitespace, the normal split() method of a string won’t work.
For this you can use shlex.split(), which preserves quoted whitespace within a string.

import shlex
cmd = 'herp derp "fuzzy bear" "wanga tanga" pop'
print(cmd.split())   # ['herp', 'derp', '"fuzzy', 'bear"', '"wanga', 'tanga"', 'pop']
print()
print(shlex.split(cmd)) # ['herp', 'derp', 'fuzzy bear', 'wanga tanga', 'pop']