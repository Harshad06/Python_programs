
l1 = ["a", "b", "c", "d","a", "b","a", "b","a", "b","c", "d","c", "d","c", "d","c", "d","c", "d"]

l2 = sorted(set(l1))
# print(l2)

for item in l2:
    count = l1.count(item)
    print(f'{item}: {count} times')
