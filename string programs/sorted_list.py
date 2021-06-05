
l1 = ["a", "b", "c", "d","a", "b","a", "e","c","e", "d","c", "e"]

new_l2 = sorted(set(l1))
print(new_l2)

for item in new_l2:
    count = l1.count(item)
    print(f'{item}: {count} times')


'''
Here if we run for loop on 'l1', then each item will be printed each time it is iterated as long as the list runs.

So we call for loop on 'new_l2', as here list is sorted --> elements are present only once as 'set' is called along with 'sorted'.

And inside for loop --> count is called on 'l1' list and items are passed.

    l1.count(items)

'''