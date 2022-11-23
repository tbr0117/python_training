## Set collection of items and unique
from typing import Set


numbers = [1,2,1,2,3,4]
uniques = set(numbers) # {1,2,3,4}
uniques.add(5) # add
uniques.remove(4) # remove
print(uniques) 

first = {1,1,2,2,3,4}
second = {1,3,5}

union_set = first | second # union on two sets
print(union_set) # {1,2,3,4,5}

inner_set = first & second # Inner join on two sets
print(inner_set) # {1,3}

diferrece = first - second # Left outer only 
print(diferrece) # {2,4}

outer_set = first ^ second # Outer only - 
print(outer_set) # {2,4,5}


if 1 in first:
    print("Yes")

