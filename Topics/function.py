def fun01():
    print("Hello Dude")


fun01()

def greet(first_name, last_name): # function with parameters
    print(f"Hello {first_name} {last_name}")
    print("Welcome to my space")


greet("MB", "BM") # call function with arguments

## Optional parameters/ Default values
## optional parameters should be end of required parameters

def increment(number, by=2): # function parameters with default vales
    return number + by


print(increment(10, by=5)) # arguments with key
print(increment(10)) # with out optional parameters


## xargs -> collection of arguments /
# * indicate that collection
def multify(x, y):
    return x * y

print(multify(2,3)) # multify take only first two values only

## * indicates collection of parameters/arguments
def multify_numbers(*numbers):  # values come with tupple like (2,3,4,5) 
    total = 1
    for number in numbers:
        total *= number # total * number
    return total


print(multify_numbers(2,3,4,5)) # can pass n numbers of argumnets


## xxargs -> collection of arguments with key's
## ** indicates that collection of arguments with keys

def update_user(**user): # values come with object/ dictionary like {'name':'Me', 'age':9}
    print(user)
    print(user["name"])


update_user(name="Me", age=9, address="here only") # arguments with keys

    
## Variable scope
## if variable declared in fucntion then scope would be with in the function only
## global varibales - would declared in file level and the scope would be 
## Note: names of varibales not unique in python means

message = "BM" # global varible
def greet_me(name):
    message = "MB"  # this is treat as local varible but not global variable, so global value can't change

greet_me("hello")
print(message) # message

def greet_me2(name):
    global message   # global - tells it's a global varible so, python don't crate local memory for the variable
    message = "TBR" # the value overwrite in globle varibale

greet_me2("MM")
print(message)


def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number


print(fizz_buzz(3))       