
# Print the numbers described in the exercise
numbers=[str(x) for x in range(1,11)] # making a list of strings containing numbers 
for i in range(len(numbers)):
    growing_str=' '.join((numbers[0:i+1])) # joining the strings of numbers 
    print(growing_str)


