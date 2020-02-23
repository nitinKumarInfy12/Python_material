#! python3
# pw.py - An insecure pasword locker program
import sys, pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345',
             }


if len(sys.argv) < 2:
    print(f"Usage: python pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1] # FIRST COMMAND LINE ARG IS TE ACCOUNT NAME
#print(f"password: {PASSWORDS[account]}")

# CHECK IF account exists in the dictionary then copy the password to clipboard
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} is copied to clipboard")
else:
    print(f"There is no account name {account}")


"""
# save the following 2 lines of code in c:\windows foder as batch file pw.bat and hit windows+r and execute pw <account name>  
@py.exe C:\Users\kumar\PycharmProjects\password_locker\pw.py %*
@pause
"""
