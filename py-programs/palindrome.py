

def isPalindrome(s):
    return s == s[::-1]

s = input(str("Enter the string : "))
res = isPalindrome(s)

if res:
    print("Yes")
else:
    print("No")