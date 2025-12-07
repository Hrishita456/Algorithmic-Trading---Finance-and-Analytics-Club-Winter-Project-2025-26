s = input("Enter a string: ")

left = 0
right = len(s) - 1
flag = 1  # assume it's palindrome

while left < right:
    if s[left] != s[right]:
        flag = 0
        break
    left = left + 1
    right = right - 1

if flag == 1:
    print("Palindrome")
else:
    print("Not Palindrome")