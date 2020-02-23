import re, sys

# q1 : write the regerx for a number with commas for every three digits
x = """
'# maust math the following'
'42'
'768'
'1,234'
'6,368,745'
'# must not mathc teh follwoing'
'12,34,567'
'1234' """

test1 = re.compile(r'''(
'\d{1,3}'|'\d*,(\d{3}).*'
)''',re.VERBOSE)

print(test1.findall(x))


# q2 print teh full name whose last name is Nakamoto
y = """
'# must match the following'
'Santoshi Nakamoto'
'Alice Nakamoto'
'Robocop Nakamoto'
'# But not the following'
'sabtoshi Nakamoto'
'satoshi Nakamoto' (where the first name is not capitalized)
'Mr. Nakamoto' (where the preceding word has a nonletter character)
'Nakamoto' (which has no first name)
'Satoshi nakamoto' (where Nakamoto is not capitalized)
'Rahul Nakamoto'
"""

test2 = re.compile(r'[A-Z]\w* Nakamoto')

print(test2.findall(y))


# q3 :write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the
# second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a
# period? This regex should be case-insensitive

z = """
'#It must match the following:'
'Alice eats apples.'
'Bob pets cats.'
'Carol throws baseballs.'
'Alice throws Apples.'
'BOB EATS CATS.'
'#but not the following:'
'Robocop eats apples.'
'ALICE THROWS FOOTBALLS.'
'Carol eats 7 cats.'
"""

test3  =re.compile(r'''(
(Alice|Bob|Carol)
\s+
(eats|pets|throws)
\s+
(apples|cats|baseballs)\.
)''', re.VERBOSE|re.I)

print(test3.findall(z))


#q4 : STRONG PASSWORD DETECTION

pswd ='Aawerthy7'
#pswd = str(input(f"Enter the password: "))
#print(len(pswd))
test4 = re.compile(r'(\w{8}\w*)',re.I)
test5 = re.compile(r'[A-Z]')
test6 = re.compile(r'[a-z]')
test7 = re.compile(r'[0-9]')
"""
if not test4.findall(pswd):
    print(f"Level1: Password is less than 8 characters")
    sys.exit()
if not test5.findall(pswd):
    print(f"Level2: Password must have upper and lower case")
    sys.exit()
    """
if not (test6.findall(pswd) and test5.findall(pswd) and test4.findall(pswd) and test7.findall(pswd)):
    print(f"Password must have upper and lower case and minimum 8 characters long and atleast one number")
    sys.exit()
else:
    print(len(pswd))
    print(f"Pass : {test4.findall(pswd)}")
    print(f"Pass : {test5.findall(pswd)}")
    print(f"Pass : {test6.findall(pswd)}")
    print(f"Pass : {test7.findall(pswd)}")

#print(test4.findall(pswd))



print(slice('ramram'))

