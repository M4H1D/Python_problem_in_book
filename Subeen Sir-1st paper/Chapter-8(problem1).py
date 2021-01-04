#This is only for upper case.But I will try all solution than question need.
def only_upper(s):

    upper_chars =""

    for char in s:

            if char.isupper():

            	upper_chars += char    return upper_chars

x=only_upper(input())

print(x)
