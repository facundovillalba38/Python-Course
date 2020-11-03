print("Welcome to the Fibonacci Calculator App")

number = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

print("The first",number,"numbers of the Fibonacci sequence are: ")
fib = [1,1]
for i in range(number-2):
     new_fib = fib[i] + fib[i+1]
     fib.append(new_fib)
print(fib)

#compute golden ratio
golden = []
for i in range(len(fib)-1):
     ratio = fib[i+1] / fib[i]
     golden.append(ratio)

print("golden ratio", golden)