# To sort a dictionary -

# this will sort by key 
c={2:3, 1:89, 4:5, 3:0}
y = sorted(c.items())
#print(y)


#Another excampple of sort by key
d = { "John":36, "Lucy":24, "Albert":32, "Peter":18, "Bill":41 }

y = sorted(d.keys())
print(y)


x = sorted(d.values())
print(x)


z = sorted(d.items())
print(z)


for k,v in d.items():    # --------> Unordered
    print(k,':',v)  


#print('Key : Value')
for k,v in sorted(d.items()):    # --------> Ordered
    print(k,':',v)