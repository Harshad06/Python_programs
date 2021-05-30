'''
Name = input("Enter your name : ")
Age = input("Enter your age : ")

print(Name, Age)
'''


# Now, concept of multiple inputs:
# Here, split happens on " " ---> a space between name and age

name, age = input("Enter your name and age : ").split()
print(name, age)