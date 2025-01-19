binary = input("Enter a binary number: ")

if '.' in binary:
    integer, frac = binary.split('.')
else:
    integer, frac = binary, ''

decimal = 0
for index, digit in enumerate(reversed(integer)):
    if int(digit) not in [0, 1]:
        print("Invalid binary number")
        exit()
    
    decimal += int(digit) * (2 ** index)

fraction = 0
for index, digit in enumerate(frac):
    if int(digit) not in [0, 1]:
        print("Invalid binary number")
        exit()
    digit = int(digit)
    fraction += digit * (2 ** -(index+1))

decimal += fraction

print("The decimal value is:", decimal)