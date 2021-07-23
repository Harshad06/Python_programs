
'''
"""
emp = [('Mathew','Hudson',35,'New York'),('Ronnie','Hugo',40,'Singapore'),('Carol','Jeffcut',55,'London')]

output = [('Mathew Hudson', 35, 'New York'), ('Ronnie Hugo', 40, 'Singapore'), ('Carol Jeffcut', 55, 'London')]
"""

emp = [('Mathew','Hudson',35,'New York'),('Ronnie','Hugo',40,'Singapore'),('Carol','Jeffcut',55,'London')]

print(emp[0]) 

new = ' '.join(emp[0])
print(new)

'''
'''

states = ['andhra pradesh','tamil nadu','utter pradesh','madhya pradesh','telangana','orissa']

output = ['Andhra Pradesh', 'Tamil Nadu', 'Utter Pradesh', 'Madhya Pradesh', 'Telangana', 'Orissa']

str1 = str(states)
print(str1)

st = [x for x in states]
# print(str1.upper())
'''
'''
emp = [('name','mark'),('age',33),('salary',55000),('country','india')]
output = {'name': 'mark', 'age': 33, 'salary': 55000, 'country': 'india'}

print(dict(emp))

'''
'''

'''
date = "2021-05-27"
expected_format = "27-May-2021"

newDate=list(date.split("-"))

newDate[1] = "May"

print(str(newDate))

#print(','.join(str(newDate)))

print(str(newDate).replace(',','-'))