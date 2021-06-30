

# PRINT PATTERN:-

n = int(input("Enter the number of rows: "))

for row in range(n,0,-1):
    for col in range(1,row+1):
        print(col, end="")
    print()

'''
output:-
Enter the number of rows: 5
12345
1234
123
12
1
'''
