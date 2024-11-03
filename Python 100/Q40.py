# Write a program which accepts a string as input to print "Yes" if
# the string is "yes" or "YES" or "Yes", otherwise print "No".

def yes_or_no(s):
    if s == 'yes' or s == 'YES' or s == 'Yes':
        print('Yes')
    else:
        print('No')