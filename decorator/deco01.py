
# Python program to illustrate functions 
# can be treated as objects

def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout    # function being treated as a object

print(yell('Hellooo'))