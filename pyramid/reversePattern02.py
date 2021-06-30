
# https://www.youtube.com/watch?v=N02bYFj5ESM&ab_channel=Amulya%27sAcademy


# PRINT PATTERN 01 :-

n = int(input("Enter the number of rows: "))

for row in range(n,0,-1):
    for col in range(1, row+1):
        print(row, end="")
    print()

'''
Enter the number of rows: 5
55555
4444
333
22
1
'''
# ----------------------------------------

# PRINT PATTERN 02 :-

n = 5 

for row in range(n,0,-1):
    for col in range(1, row+1):
        print(row, end="")

# output: 555554444333221