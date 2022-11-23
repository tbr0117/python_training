## List collection of objects
## objects like string, number, boolean, float, list, Dictionary/Object
## ["a","B",2,True,3.5,["b","b"],"F"]  Doesn't care abt type of objects

from typing import Sequence


leters = ["a", "b", "c", "d"]
num    = [1,2,3,4,5]
matrix = [[0,1], [2,3]]

## simple ways to do lists
## Multipy set of objects 
list_zeros = [0] * 5 # [0,0,0,0,0]
print(list_zeros)
list_numbers = [1,2] * 5  # [1,2,1,2,1,2,1,2,1,2,1,2]
print(list_numbers)

## combine /merge lists
combined_list = leters + list_zeros # ["a","b","c","d","0","0","0","0","0"]
print(combined_list)

## range to list of numebrs
numbers = list(range(1,20)) # [1,2,....,19]
print(numbers)

## string to list
characters = list("Python World") # ["P","y",...," ","W",...,"d"]
print(characters)


## Accessing / Pointing items of list
## ["a","b","c","d","e"]
##   0   1   2   3   4     <- forward index
##  -5  -4  -3  -2   -1     <- Backward index

letters = ["a","b","c","d","e"]
letters[0]   # "a"
letters[-1]  # "e"
letters[0:3] # ["a", "b", "c"]
letters[:3]  # ["a", "b", "c"]
letters[2:]  # ["c", "d", "e"]
leters[-2]   # "d"
letters[0] = "A" # change value in index 0
letters[::2]     # ["a", "c", "e"] # return every second items
print(letters[::2])

print(letters[:-1]) #  ["a", "b", "c", "d"] - 
letters[0:-2] # ["a", "b", "c"]

## :: list reverse order
print(letters[::-1]) # ["e", "d","c","b","a"] - reverse order
print(letters[::-2]) # ["e", "c", "a"] - reverse order every second item
print(letters[1::-2]) # ["b"]

start_index = 2
end_index = 8
print(letters[start_index:end_index]) # with dynamic index

## Unpaking lists
numbers = [1,2,3]
first, second, third = numbers  # numbers of variables shoud equal to number of list items RHS = LHS
print(second) # first = numbers[0] = 1
              # second = numbers[2] = 2
              # third = numbers[3] = 3

numbers = [1,2,3,4,5,6,7,7,7,7,9]
first, second, *others = numbers # * - collect / packing all remaining items of list
print(second)
print(others) # [3,4,5,6,7,7,7,7,9] 

first, *others, last = numbers # separate first & last ones
print(first, last) # 1, 9
print(others) # [2,3,4,5,6,7,7,7,7] 


## Looping
## for loop
letters = ["a","b","c","d","e"]
string = ""
for letter in letters:
    string += letter
print(string)   # abcde

for letter in enumerate(letters): # enumeration - numbering items onr by one 
    # enumetate retun values in tupple like (0, "a") (1, "b") (2, "c")
    index, value = letter # unpack value and index
    print(index, value) #

for index, value in enumerate(letters): # Same result of previous for loop 
    # unpacked enumerate items
    print(index, value)



## Adding // Removing items
## Add
letters = ["a","b","c","d","e", "f"]
letters.append("g") # append at end
letters.insert(0, "-") # insert at index
print(letters)

## Remove
letters.pop() # Remove last item
letters.pop(0) # remove item at index
letters.append("c")
letters.remove("c") # remove fist item of matched given value
print(letters)
del letters[0] # delete item of given index
del letters[0:3] # delete items of given index range
print(letters)
letters.clear() # clear all items in list


## Finding items
letters = ["a","b","c","d","e","f"]
# # index() will raise error when given value not exist in list 
print(letters.index("d")) # return index of value
print(letters.count("d")) # return count of matched valus
if "g" in letters:
    letters.index("g") # the will raise error if value not exist in list

## Sorting
numbers = [3,54,23,98,5,41]
numbers.sort() # sort to ascending order in list itself
numbers.sort(reverse=True) # sort descending order
print(numbers)
numbers_1 = [3,54,23,98,5,41]
numbers_s1 = sorted(numbers_1, reverse=True) # sorted fuction will return sorted list
print(numbers_s1)
print(numbers_1)

## sort on complex item str
product_list = [("product1", 30), ("product2", 10), ("product3", 59)]

def sort_item_by_price(item): # custom fucntion for determine sort value
    return item[1] # return price value of product

print(sorted(product_list, key=sort_item_by_price, reverse=True )) # pass function in key

material_list = [{"product": "Prodcut1", "price": 30 }, 
                {"product": "Prodcut1", "price": 10 }, 
                {"product": "Prodcut1", "price": 50 }]
def sort_by_price(obj): # fucntion for return price value
    return obj["price"]

print(sorted(material_list, key=sort_by_price, reverse=True)) # sort list object with custom function

## Lambda expression or function
#3 inline fucntion / inline expression
## syntax -> lambda <parameters>:<expression>

material_list.sort(key=lambda obj: obj["price"], reverse=True) # simply specify inline lambda expression
print(material_list)

print(sorted(product_list, key=lambda item: item[1])) # inline exoresion

## Map
## map fucntion retun map object so we should use list method to get result in list format 
# map object like <map object at 0x000001BBC45F53A0>
price_list = list(map(lambda item:item[1], product_list)) # map iterate list 
print(price_list)

def product_obj_map(item):
    return {
        "mat": item[0],
        "price": item[1]
    }

print(list(map(product_obj_map, product_list))) # custom function to map

## Filter
# filter fucntion return filter object so, we should use list method to get result in list format
product_list = [("product1", 30), ("product2", 10), ("product3", 59), ("product3", 25)]

filter_obj = filter(lambda item:item[1] >= 30, product_list)
print(filter_obj) # filter object like <filter object at 0x000001BBC45F53A0>
print(list(filter_obj)) # conver list

## List Comprehensions
## syntax: [<expression> for item in <items>]
## syntax: [<expression> for item in <items> if <expression>]

#price_list = list(map(lambda item:item[1], product_list))
prices_m1 = [item[1] for item in product_list] # short way to map 
print(prices_m1)
print([item[1] for item in product_list if item[1] >= 30 ])

## Zip function
## zip combine multiple lists to single list with tuples
## zip return zip object so we shuld use list method to get result in list
## also return values only upto equal index of all lists
list1 = [1,2,3,4]
list2 = [10,20,30]
zip_list = zip(list1, list2) # [(1,10), (2,20), (3,30)]
print(list(zip_list)) 

print(list(zip("abcde", list1, list2, "uvwzyz")))


## Stacks
## LIFO = Last In - Fisrt Out
browsing_session = []
browsing_session.append(1) # Append to 
browsing_session.pop()  # fisrt out
if browsing_session:
    print(browsing_session[-1]) # set current / latest one

## Queues 
## FIFO = First In - First Out
[1,2,3,4] # if one out
[2,3,4] # here all other objects needs to change memory locations

from collections import deque
queue = deque([])
queue.append(1) # in - add queue
queue.append(2)
queue.append(3)
queue.popleft() # first out
print(queue)
if not queue:
    print("empty queue")
