n = int(input("enter how many numbers: "))

numbers = []

for i in range(n):
    x = int(input("enter a number: "))
    numbers.append(x)

# set first number as both max and min
maximum = numbers[0]
minimum = numbers[0]

# check each number one by one
for i in range(n):
    if numbers[i] > maximum:
        maximum = numbers[i]
    if numbers[i] < minimum:
        minimum = numbers[i]

print("maximum =", maximum)
print("minimum =", minimum)
