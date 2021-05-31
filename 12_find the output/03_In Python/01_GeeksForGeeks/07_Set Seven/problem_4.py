print('C:\\inside C directory')  # statement1

print(r'C:\\inside C directory')  # statement2
# Raw strings do not treat the backslash as special characters at all.

print('\x25\x26')
"""
In the above code "[\ x]" is an escape sequence that means the following 2 digits are
a hexadecimal number encoding a ncharacter. Hence the corresponding symbols will 
be on the output screen.
"""
