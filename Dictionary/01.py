
emp1 = {'fname': 'Harshad'}
emp2 = {'lname': 'Shringi'}

emp = emp1['fname'] + ' ' + emp2['lname']
print(emp)              # Harshad Shringi

emp1.update(emp2)
print(emp1)            # {'fname': 'Harshad', 'lname': 'Shringi'}
