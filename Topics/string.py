## strings methods
# len() -> length of string
# string[pos:pos] -> sub string 

from typing import Counter


var_string = "Hello"

# print(len(var_string))
# print(var_string[0])
# print(var_string[1])
# print(var_string[-1])
# print(var_string[-2])
# print(var_string[1:5])
# print(var_string[1:1])
# print(var_string[1:-1])

# """ -> thriple coutes -> used for message or long text with multiple lines 
message = """ Hello
New Next line  
Hello John,

This TB,

Blah blah ....."""

print(len(message))
# print(message[0:])
# print(message[10:len(message)])
# print(message[10:-10])


# Escape Sequences
# \" -> "
# \' -> '
# \\ -> \
# \n -> new line

print("Python \"Program\"")
print("Python \'Program\'")
print("Python \nProgram\\")

## concate / format
first = "Bhargava"
last = "Tanguturi"

fullname = first + " " + last

# f"" / F"" - formted string 
fullname_1 = f"{first} {last}"
fullname_2 = F"{last} {first}"

print(fullname)
print(fullname_1)
print(fullname_2)

my_string = "   pyTHon prograMing  "
# upper - returns upper case string
print(my_string.upper())
# lower - returns lower case string
print(my_string.lower())
# title - returns title format string
print(my_string.title())
# strip - remove white spaces and retrun string
print(my_string.strip())
print(my_string.rstrip())
print(my_string.lstrip())
# find - returns index of sub string
print(my_string.find("pr"))
# replace - replace sub string and return string
print(my_string.replace("pr", "BM"))

# expression to check string  - return boolean vlaue
print("pr" in my_string)
print("BM" not in my_string)


