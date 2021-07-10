
# Python3 program to find first
# repeating element in arr[]

# This function prints the first repeating element in arr[]
def printFirstRepeating(a, n):
	for i in range(len(a)):
		if a.count(a[i]) > 1:
			return a[i]
	return "there is no repetition number"


# Driver code
arr = [10, 5, 3, 4, 3, 5, 6]
n = len(arr)
print(printFirstRepeating(arr, n))