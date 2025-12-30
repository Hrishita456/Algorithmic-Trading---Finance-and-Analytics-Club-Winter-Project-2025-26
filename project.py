#Question 1
n = int(input("Enter number of elements: "))

arr = [];
print("Enter the elements:")
for i in range(0,n,1):
    arr.append(int(input()))

maximum = arr[0]
minimum = arr[0]

for x in arr:
    if x > maximum:
        maximum = x
    if x < minimum:
        minimum = x

print("Maximum =", maximum)
print("Minimum =", minimum)

#Question 2
s = input("Enter a string: ")

s = s.lower()

left = 0
right = len(s) - 1

is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#Question 3
n = int(input("Enter number of elements: "))

arr = []
print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))


x = int(input("Enter the value of x: "))

arr.sort()

for i in range(0,n,1):
    for j in range(i,n,1):
        if arr[j]-arr[i]==x:
            print(arr[i],"&",arr[j])
    


