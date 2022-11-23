### use input() method for input values
## default type of input string

# x = input() 
# print(type(x))
# print(x)

# name = input("name: ")
# print(f"you entered name: {name}")

## Types & Conversions
## type() -> tells type of value

# String - str()
# Integer - int()
# Boolean - bool()
# Float - float()

number = input("number: ")
print(f"number + 5: { int(number) + 5 }")


float_number = input("float Numebr: ")
value1 = float(float_number) + 5.5
print(f"value + 5.5: {value1}")

value = input("value: ")
value_boolean = bool(value)
print(value_boolean)

## boolean value
## Falsy = if input value is: "", 0, None
print(bool(""))
print(bool(0))
print(bool(None))

## True values - if input contains any character or number except 0
print(bool(1))
print(bool(-1))
print(bool("False"))
print(bool(" "))

