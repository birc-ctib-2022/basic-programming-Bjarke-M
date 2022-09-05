
# Print the pattern
emptystr=''
for i in range(10):
    if i<5:
        emptystr+=' *'
        print(emptystr)
    elif len(emptystr)-2!=0:
        emptystr=emptystr[:len(emptystr)-2]
        print(emptystr)
    else:
        break
