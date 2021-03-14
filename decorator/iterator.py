
my_list = [10,20,30,40,50,60]

it = iter(my_list)

while True:
    try:
        print(next(it))
    except StopIteration:
        break