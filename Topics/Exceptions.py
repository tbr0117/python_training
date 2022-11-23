# number = input("enter any:")

# try:
#     print(int(number) + 123)
# except TypeError:
#     pass
# except ValueError:
#     print(f"Expected numeric values only not: {number}")
#     print(123)

# Control break / process break/ block break
# return
# break
# continue
# pass

# return

def myFuxntion_123(a):
    if type(a) != dict:
        raise TypeError
    # ur logic
    b = a.name  # expected value for "a" is dict / class
    c = b[2:10]


def myFuxntion(somting):
    new_value = myFuxntion_123(somting)
    # ur logic
    new_value = new_value + 121
    return new_value


mynum = 10
try:
    value = myFuxntion(mynum)
except TypeError:
    pass

print("executed successfully")
