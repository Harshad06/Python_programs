
# Problem 1 
emp = [('Mathew','Hudson',35,'New York'),('Ronnie','Hugo',40,'Singapore'),('Carol','Jeffcut',55,'London')]

output = [('Mathew Hudson', 35, 'New York'), ('Ronnie Hugo', 40, 'Singapore'), ('Carol Jeffcut', 55, 'London')]


res = [[' '.join(item[0:2]), *item[2:]] for item in emp]
#print(res)




# Problem 2 
states = ['andhra pradesh','tamil nadu','utter pradesh','madhya pradesh','telangana','orissa']

output = ['Andhra Pradesh', 'Tamil Nadu', 'Utter Pradesh', 'Madhya Pradesh', 'Telangana', 'Orissa']

res = [item.title() for item in states]
#print(res)



# Problem 3
# Convert to a dictionary 
emp = [('name','mark'),('age',33),('salary',55000),('country','india')]

output = {'name': 'mark', 'age': 33, 'salary': 55000, 'country': 'india'}

res = dict(emp)
#print(res)




# Problem 4
import dateutil.parser

date = "2021-05-27"
expected_format = "27-May-2021"

print(dateutil.parser.parse(date).strftime("%d-%b-%"))