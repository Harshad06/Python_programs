
from typing import Counter

s  = 'hi hello hi hello welcome hello hi hello welcome'
ss = s.split()
print(ss)

d = Counter(ss)
print(d)
