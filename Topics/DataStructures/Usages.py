## Unpacking
list_1 = [1,2,3,4]
list_2 = [4,5]
print(*list_1)
all_num = [*list_1, *list_2] # [1,2,3,4,5]
print("all num:", all_num)

mixed_list = [*list_1, *"ABC", *list_2, *"END"] # [1,2,3,A,B,C,4,5,E,N,D]
print("Mixed List:", mixed_list)

set_1 = {1,2,3}
set_2 = {4,5}
all_set = {*set_1, *set_2} # {1,2,3,4,5}
print("all_set:", all_num)

print("mixed set:", {*set_1, *"ABC", *set_2, *[9,8,6,"END"]})

dictionarie_1 = {"x": 1, "y": 2}
dictionarie_2 = {"y": 10, "z": -20}
all_disctionarie = {**dictionarie_1, **dictionarie_2} # {"x": 1, "y": 10, "z": -20}
print("all disctionaries:", all_disctionarie) 
all_keys = {*dictionarie_1, *dictionarie_2} # {"x", "y", "z"}
print("all keys:", all_keys)


## Comprehensions
numbers = [1,2,3,4,5]

list_num = [num * 2 for num in numbers] # [2,4,6,..]
set_num = {num *2 for num in numbers} # {2,4,6,...}
dist_num = {num: num *2 for num in numbers} # {1: 2, 2: 4, 3: 6, ...}
print("list_num", list_num)
print("set_num", set_num)
print("dist_num", dist_num)

