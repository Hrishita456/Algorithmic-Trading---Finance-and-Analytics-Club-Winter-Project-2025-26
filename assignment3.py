n = int(input("Enter how many numbers: "))
arr = []

for i in range(n):
    a = int(input("Enter a number: "))
    arr.append(a)

x = int(input("Enter the value of x: "))

# Sort the list
arr.sort()

left = 0
right = 1
found = False

while right < n:
    diff = arr[right] - arr[left]

    if diff == x:
        print("Pair found:", arr[left], "and", arr[right])
        found = True
        break

    # If difference is too small, increase right
    if diff < x:
        right = right + 1
    else:
        left = left + 1

    # Make sure left and right do not overlap incorrectly
    if left == right:
        right = right + 1

if not found:
    print("No pair found")   # (but question says pair always exists)
    