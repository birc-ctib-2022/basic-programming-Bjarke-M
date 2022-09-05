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
for i in password:
    upper, lower, nummeric, character, length=0,0,0,0,0
    if i.isupper()==True:
        upper=+1
    if i.islower()==True:
        lower+=1
    if i.isnumeric()==True:
        nummeric+=1
    if i in ['$#@']:
        character+=1
    if 8<len(password)<16:
        length+=1
    if upper and lower and nummeric and character and length != 0:
        is_valid = True

print(is_valid)
