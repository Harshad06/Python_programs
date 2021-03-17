

s = "wowow"
rev = "".join(reversed(s))
print(s)
print(rev)


'''
Only printing "reversed(s)" will give --- <reversed object at 0x01C1E700>
but rev = "".join(reversed(s))  will give string.
'''

if s == rev:
    print(f'Yes')
else:
    print(f'No')