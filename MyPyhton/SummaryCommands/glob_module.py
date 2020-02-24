# Using glob
• Expands wildcards
• Windows and non-windows
• Useful with subprocess module
When executing external programs, sometimes you want to specify a list of files using a wildcard. 

The glob function in the glob module will do this. Pass one string containing a
wildcard (such as *.txt) to glob(), 

# it returns a sorted list of the matching files. If no files match, it returns an empty list.

from glob import glob

files = glob('../DATA/*.txt') ①
print(files)