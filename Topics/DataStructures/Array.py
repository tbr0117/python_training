## Array are similar of list
## array are type dependent object means, every item should be same type
## Array are best with large amount of data, performance 
##
## import array module from liberay

from array import array

numbers = array("i", [1, 2, 3, 4])
numbers.append(5)

print(numbers)

numbers.append(454)