# regular expression or regex. use it from re module
# \d\d\d-\d\d\d-\d\d\d\d is analogus to 123-345-2345 where \d represents digit character
# \d{3}-\d{3}-\d{4} also is analogus to 123-345-2345

import re

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

# can be used with multiple assignment to seperate the values
areaCode, mainNumber = mo2.groups()

print(f"Area code: {areaCode}")
print(f"Main number: {mainNumber}")

print('=================()====================')

"""Parentheses have a special meaning in regular expressions, but what do you do if you need
to match a parenthesis in your text? For instance, maybe the phone numbers you are trying
to match have the area code set in parentheses. In this case, you need to escape the ( and )
characters with a backslash"""

message = 'My phone number is (415) 555-4242.'
phoneNumRegex3 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo3 = phoneNumRegex3.search(message)
print(f"Area code: {mo3.group(1)}")
print(f"Main number: {mo3.group(2)}")
print(f"Phone nummber: {mo3.group()}")

print('=================pipe match one of many expressions====================')



# Matching Multiple Groups with the Pipe |
# the regular expression r'Batman|Tina Fey' will match either'Batman' or 'Tina Fey'.
# When both Batman and Tina Fey occur in the searched string, the first occurrence of matching text will be returned
#find all matching occurrences with the findall() method
textString = 'Batman and Tina Fey'
pipeEx = re.compile(r'Batman|Tina Fey')
searchObj = pipeEx.search(textString)
print(f"{searchObj.group()}")

textString = 'Tina Fey and Batman'
pipeEx = re.compile(r'Batman|Tina Fey')
searchObj = pipeEx.search(textString)
print(f"{searchObj.group()}")

# in case of multiple similar pattern, a prefix can be specified for all words
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
# 'Batmobile'
print(mo.group(1))
#'mobile'

#If you need to match an actual pipe character, escape it with a backslash, like \|
print('===========Optional Matching with the Question Mark ?===========================')
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
#'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#'Batwoman'

# Using the earlier phone number example, look for phone numbers that do or do not have an area code
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
#'415-555-4242'
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())
#'555-4242

#If you need to match an actual question mark, escape it with a backslash, like \?
print('==========Matching Zero or More with the Star============================')
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
#'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
#'Batwoman'
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
#'Batwowowowoman'

#If you need to match an actual question mark, escape it with a backslash, like \*
print('==============Matching One or More with the Plus========================')
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
#'Batwoman'
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
#'Batwowowowoman'
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)
#True

#If you need to match an actual + mark, escape it with a backslash, like \+
print('===========Matching Specific Repetitions with Curly Brackets{}===========================')
# (Ha){3} : (Ha)(Ha)(Ha)
#And these two regular expressions also match identical patterns:
#(Ha){3,5} : ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
#'HaHaHa'
mo2 = haRegex.search('Ha')
mo2 == None
# True
print('=============Greedy and Nongreedy Matching with ? mark=========================')
# greedy (default) returns the longest string possible
# non-greedy with ?, returns the shortest match string possible
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
print(f"groups: {mo1.groups()}")
#'HaHaHaHaHa'

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())
print(f"groups: {mo2.groups()}")
#'HaHaHa'

#question mark can have two meanings in regular expressions: declaring a nongreedy match or flagging an optional group


print('==============findall()=====returns all matched patters===================')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(f"Search() output : {mo.group()}")
#'415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(f"findall() output: {mo}")
#['415-555-9999', '212-555-0000']

#if the regex object has groups then findall returns list of tuples
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(f"findall() output with groups in regex pattern: {mo}")
#[('415', '555', '1122'), ('415', '555', '8899')]

print('======================================')
#(\s*(ext|x|ext.)\s*\d{2,5})?
testregerx = re.compile(r'(\s*)')

print(f"test result is: {testregerx.search('myphoneext.is0124').groups()}")

if(testregerx.search('myphoneext.is0124').groups()):
    print (f"pass :{len(testregerx.search('myphoneext.is0124').groups())}")
print(len('myphoneext.is0124'))
print('======================================')
numRegex = re.compile(r'\d+')
print(numRegex.sub('X', '12 drummers, 11 pipers, fiverings, 3 hens'))
print('======================================')

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