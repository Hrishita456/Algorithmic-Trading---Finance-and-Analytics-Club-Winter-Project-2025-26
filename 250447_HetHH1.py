
n = int(input("How many numbers? "))

# Read first number (we need at least one number)
first = int(input())
max_val = first
min_val = first

# Read the remaining (n-1) numbers
for i in range(n-1):
    x = int(input())
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x

print("Maximum:", max_val)
print("Minimum:", min_val)