
l1 = ["a", "b", "c", "d", "e", "a", "b", "c", "d", "e"]

l2 = sorted(set(l1))

for item in l1:
    count = l1.count(item) 
    print(f'{item}:{count} times')