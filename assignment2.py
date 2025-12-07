s = input("Enter a string: ")

left = 0
right = len(s) - 1

is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left = left + 1
    right = right - 1

if is_palindrome:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
