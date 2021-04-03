
def isPalindrome(s):
    return s == s[::-1]

s = input(str("Enter the string : "))
result = isPalindrome(s)

if result:
    print("Yes")
else:
    print("No")


'''
s = "wowow"
rev = "".join(reversed(s))
print(s)
print(rev)

            ------------
          |  # Only printing "reversed(s)" will give --- <reversed object at 0x01C1E700>
          |  # but rev = "".join(reversed(s))  will give reverse string.
            ------------

if s == rev:
    print(f'Yes')
else:
    print(f'No')

'''