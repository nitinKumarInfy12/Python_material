#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

#print(text)


# separate lines and add stars
lines = text.split('\n')
for line in lines:
    line = f"* {line}"  # add star to each string iin lines list
    print(line)
text = '\n'.join(lines)
pyperclip.copy(text)