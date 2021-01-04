import re
String =input("Enter a string: ") 
def split_upper_lower_digit_symbols(input):
    upper = ''.join([x for x in input if x.isupper()])
    lower = ''.join([x for x in input if x.islower()])
    digit = ''.join([x for x in input if x.isdigit()])
    symbols = ''.join(re.sub('[^$#+!@%^&*(){}].,?|\/', '', String))
    
    return upper,  lower, digit,symbols

print(split_upper_lower_digit_symbols(String))
