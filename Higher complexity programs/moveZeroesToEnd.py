

# move all zeroes to the end:-

lst  =  [1,7,0,0,10,12,0,5,6]

l1 = [x for x in lst if x!=0]
l2 = [x for x in lst if x==0]

print(l1+l2)       # [1, 7, 10, 12, 5, 6, 0, 0, 0]