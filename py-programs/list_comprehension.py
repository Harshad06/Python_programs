
# To print 10 even no.s
l1 = [2*e for e in range(1,11)]
print(l1)

# extract  even no.s from list
my_list = [23,44,56,66,78,82,85,89,92,97,100]

l1 = [e for e in my_list if e%2 == 0]
print(l1)

# fruits which have letter "a"
fruits = ["apple", "banana", "kiwi", "orange", "guava", "chikoo","strawberry"]

f = [x for x in fruits if "a" in x]
print(f)