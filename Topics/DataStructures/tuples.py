## Tuples
## similar list will accessing item / values
## Read only list
## sequence of objects we can't add / remove / modify an object sequence

## Note: the tuples are used to pass list of data with out change sequence of order at any point 

point = (1,2) # (x, y)
point_1 = 1,2 # (1,2)
point_2 = 3, # (3,)
print(type(point_2)) # <class 'tuple'>
print(point_2)
print(point)

merge_point = (1,2) + (4,5) # (1,2,4,5)
print(merge_point)
repeat_point = (1,2) * 3 # (1,2,1,2,1,2)
print(repeat_point)

tuple_list = tuple([1,2,3,4]) # (1,2,3,4)
print(tuple_list)

print(tuple("Hello Python")) # ('H', 'e', 'l', 'l', ......, 'h', 'o', 'n')

number_point = (1,2,3,4,5)
print(number_point[0]) # 1 index 0
print(number_point[0:2]) # (1,2) select range

## Un packing 
x, y, *others = number_point # 1 2 [3,4,5]

print(x, y, others)

if 5 in number_point: # condition
    print("exist")

## Swaping Variables

x = 10
y = 20

y, x = x, y # swaping like, paking tuple and un packing tuple
print(x,y) # (20, 10)

a, b = 2,3