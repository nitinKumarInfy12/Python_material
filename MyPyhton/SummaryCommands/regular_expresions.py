# regular expression or regex. use it from re module
# \d\d\d-\d\d\d-\d\d\d\d is analogus to 123-345-2345 where \d represents digit character
# similarly there are many shorthand characters
# \d{3}-\d{3}-\d{4} also is analogus to 123-345-2345 and ext 231 and 235-098-4563 ext 234 and nbi.kumar@gmail.com

# study in details in "Automate the boring stuff" book, project7 "Pattern matchin with regular expression"
import re
re.compile(<format>)
search('string'). findAll(), sub(), group(), groups()

message = 'my phone number is 123-345-4567'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # create a regex object withthe desired pattern
mo = phoneNumRegex.search(message) # it returns teh match object else none
print(f"Phone number found : {mo.group()}") # group method retunrs the actual matched text

# group() can have arguments like, 0,1,2... that returns teh matched text groups based on the regex object patern set
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo2 = phoneNumRegex2.search(message)
print('=================group()=====================')
print(f"Phone number found: {mo2.group()}")
print(f"Phone number found: {mo2.group(0)}")
print('======================================')
print(f"Area code: {mo2.group(1)}")
print(f"Remaining phone number: {mo2.group(2)}")

print('================groups()======================')
# groups()  returns all groups at once in tuple
print(mo2.groups())

#==================================== verbose mode for sub()==================
#Now instead of a hard-to-read regular expression like this:
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
#you can spread the regular expression over multiple lines with comments like this with everbose mode (''' ...''', re.VERBOSE):
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # area code
(\s|-|\.)?                      # separator
\d{3}                           # first 3 digits
(\s|-|\.)                       # separator
\d{4}                           # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?    # extension
)''', re.VERBOSE)

#if you want a regular expression that’s case-insensitive and includes newlines to match the dot character, you would form your re.compile() call like this:
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
#All three options for the second argument will look like this:
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)



"""
Shorthand character class Represents
\d Any numeric digit from 0 to 9.
\D Any character that is not a numeric digit from 0 to 9.
\w Any letter, numeric digit, or the underscore character. (Think of this as matching “word”characters.)
\W Any character that is not a letter, numeric digit, or the underscore character.
\s Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S Any character that is not a space, tab, or newline.

here’s a quick review of what you learned:
The | matches (first|second) fist or second or similary. bitwise or operator
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a nongreedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
wildcard character: "." The . matches any character, except newline characters.
"anything, everything" ".*" the .* returns everything, as . says any character and * says 0 or more
.* is greedy mode. .*? is non greedy ,mode
By passing re.DOTALL as the second
argument to re.compile(), you can make the dot character match all characters, including the newline character. re.compile('.*', re.DOTALL)
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[a-zA-Z.]{2,4} matches anything from a-z and . and 2-4 counts
[^abc] matches any character that isn’t between the brackets.
r'^abc' matches the string that starts with abc
r'abc$' matches the string that ends with abc. "carrots costs dollar"
To make your regex case-insensitive, you can pass
re.IGNORECASE or re.I as a second argument to re.compile()  
re.VERBOSE as a second parameter to compile(), to enable the verbose mode.
Note :that inside the square brackets, the normal regular expression symbols are not interpreted as such. 
This means you do not need to escape the ., *, ?, or () characters with a preceding backslash.
For example, the character class [0-5.] will match digits 0 to 5 and a period. You do not need to write it as [0-5\.]
but outside the square brackets, it needs backslash fro example : (\.[a-zA-Z]{2,4})
"""