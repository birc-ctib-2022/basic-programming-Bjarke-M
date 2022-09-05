
# Print the pattern
emptystr=''
for i in range(10):
    if i<5:
        emptystr+=' '.join('*')
        print(emptystr)
    elif len(emptystr)-1!=0:
        emptystr=emptystr[:len(emptystr)-1]
        print(emptystr)

