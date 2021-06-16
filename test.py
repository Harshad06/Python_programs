
old_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69, 'G': 67, 'H': 23}

new = { (v,k) for k,v in old_dict.items()}
print(new)