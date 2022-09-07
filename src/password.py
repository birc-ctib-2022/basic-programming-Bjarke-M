from curses.ascii import isupper
from pickle import TRUE
from re import T
import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.
is_valid= False
upper,lower,numeric,character= False,False,False,False
for i in password:
    if not 8<=len(password)<=16:
        break
    if not upper:
        upper=i.isupper()
    if not lower:
        lower=i.islower()
    if not numeric:
        numeric=i.isnumeric()
    if not character:
        character= i in ['$','#','@']

is_valid=all([upper,lower,numeric,character])
print(is_valid)
