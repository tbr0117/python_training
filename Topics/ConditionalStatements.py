## conditional statements like 
## if - if <condition/expression>: 

# In python, block code identified with indentation(spaces/tab)
temp = 10
if temp >= 10:
    # if block start
    print(f"if: {temp} >= 10")
# end if block
print("End")    


temprature = int(input("temprature: "))

if temprature > 30:
    print("It's Hot")
    print("Drink Water or Coke or Beer")
elif temprature >= 20:
    print("It's Cool")
    print("Drink Beer or Wine")
else:
    print("It's Cold")
    print("Drink Wiskhy or Vodka")
# here end the if block
print("Enjoy Your Day")

##  Ternary Operator
age = int(input("age: "))

if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

message1 = "Eligible" if age >= 18 else "Not Eligible" # same as previous if cond
print(message1)

## Chaining comparision operators
if age >= 18 and age < 60:
    message = "Eligible"
else: 
    message = "Not Eligible"

if 18 <= age < 60:   # Same result like privous if
    message = "Eligible"
else: 
    message = "Not Eligible"


## Logical Operators
## and / or / not

high_income = True  
has_credit = False
is_student = True

if high_income and has_credit:
    print("Elgibile")
elif (high_income or has_credit) and not is_student: 
    print("Check for Eligible")
else: 
    print("Not Eligible")
