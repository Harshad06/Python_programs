
# Merge 2 dictionaries in Python

x = {'a': 100, 'b': 200}
y = {'b': 300, 'c': 400}

z = {**x,**y}
print(z)            # {'a': 100, 'b': 300, 'c': 400}     overrides latest value provided