

mystr = input("Enter the string: ")
len = len(mystr)

for row in range(len):
    for col in range(0,row+1):
        print(mystr[col], end="")
    print()         #--->for new line<---