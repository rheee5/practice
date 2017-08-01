#! python3
# pw.py this program will copy a password from an account that the user types in. it will not be secure, but work as a locker

PASSWORDS = {'email': '1a2a3a4a5a6a',
             'website': 'b1b2b3b4b5b6',
             'locker': '19192928'}

import sys
import pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
