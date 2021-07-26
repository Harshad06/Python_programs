
a = {1:'abc'}
b = {2:'xyz'}

del a           # -------> dict a deleted
b.clear()       # -------> dict b contents cleared

#print(a)
#print(b)


# ------------------------------------------------

people = {
          1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}
        }

#print(people.keys())
#print(people.values())

people[1]['Name'] = "JOHNNY"

# print(people[1]['Name'])


people[1]['NAAM'] = people[1]['Name']
del people[1]['Name']

print(people)

print(people[1].values())