
# Print the pattern
# should work now
n=10
for i in range(1,n): # loop over number size of pattern
    if i<1/2*n+1:
        a_string=' '.join(['*']*i) #add * and join them with spaces (should ensure that there's no spaces at the ends)
        print(a_string)
    else:
        no_s_str=a_string.replace(' ','') #remove spaces
        smaller_str=no_s_str[:n-i] #remove one *
        result=' '.join(smaller_str) #join str again with 
        print(result)