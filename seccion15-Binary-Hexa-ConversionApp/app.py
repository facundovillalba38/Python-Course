# App to convert a decimal number into a binary or hexadecimal number


print("Welcome to the Conversion App")

maxValue = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))

decimal = list(range(1, maxValue+1))
binary = []
hexadecimal = []

for num in decimal:
     binary.append(bin(num))
     hexadecimal.append(hex(num))
print("decimal","binary","hexadecimal")

for d,b,h in zip(decimal, binary, hexadecimal):
     print(d,"\t",b,"\t",h)

