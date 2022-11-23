## Handling Exceptions

## Catch Exceptions
try:
    age = int(input("Are: "))
    xfactor = 10 / age
except ValueError as exObject:
    print("you didn't enter valid age.")
    print(exObject)
except ZeroDivisionError as ex:
    print("Age shouldn't be 0")
    print(ex)

numbers = ["a", "b", 3]
iIndex = 1
while iIndex < 4 :
    try:
        print("index 3:", numbers[iIndex])
        float = float(numbers[iIndex])
    except IndexError:
        print(f'There no item exist with index {iIndex}')
    except (ValueError, TypeError) as ex:  ## Multiple type of exceptions
        print("error while value convert")
        print(ex)
    else:
        print(f"no exception for index {iIndex}")

    iIndex += 1 

## Variable cleanup at end of try

try:
    file = open("test.py") ## load file 
    list_lines = list(file) # just lines of code
    print(list_lines)

    long_text = str(list_lines)
    num = int(age)
except FileNotFoundError:
    print("File not found")
except (NameError, IndentationError, IndexError):
    print("Some code error")
else:
    print("No error")    
finally: ## final things:, clean up
    file.close() ## Close file
print(file)


## with - used to create external resource object and clear with in try block
list_lines = []
try:
   with open("test.py") as file: ## statement same as previous one
        list_lines = list(file) # just lines of code
   long_text = str(list_lines)
except FileNotFoundError:
    print("File not found")
print(file)



## Raise Exception

def calculate_xfactor(number):
    if number <= 0:
        raise ValueError("number should be greterthan 0")
    return 10 / number


try:
    print("by 5: ", calculate_xfactor(5))
    print("by 0", calculate_xfactor(0))
except ValueError as ex:
    print(ex)
    pass ## is continue statement


## Cost of Raising Exception is very high
## So max try to avoid Raise exeception. instead, that check condition before proceed

from timeit import timeit ## used to run script and calculate time

## example some code

code1 = """
def calculate_xfactor(number):
    if number <= 0:
        raise ValueError("number should be greterthan 0")
    return 10 / number

try:
     # by5 = calculate_xfactor(5)
    by0 = calculate_xfactor(0)
except ValueError as ex:
    pass ## to pass statement
"""

code2 = """
def calculate_xfactor(number):
    if number <= 0:
        return None ## None is null object
    return 10 / number

# by5 = calculate_xfactor(5)
# if by5 == None:
#     pass
by0 = calculate_xfactor(0)
if by0 == None:
    pass
"""

print("code1: ", timeit(code1, number=10000)) ## run code1 10000 times and check time
print("code2: ", timeit(code2, number=10000)) ## run code2 10000 times