## Strings
myString = "dsfdsfdsfdsfsd"
myName = "Reddi"
dynString = f"my name is { myName }" 
dynString1 = F"" 
print(dynString)



## pass
from numpy import number


def studentInfo():
    pass

def EmployeeInfo():
    print("Hello")

if __name__ == "__main__":
    pass
else:
 print(" ElSe")


## use of extractor - > destructuring
# tupple
myNumbers = (1,2,3,4,5,6,7,8)

a = myNumbers[0]
b = myNumbers[1]
c = myNumbers[2]
d = myNumbers[3]


e,f,g,*h = myNumbers
print(f"g: {g}, h: {h}")

# print( f"c: {c}; g: {g}" )

# # List
# myNumbers1 = [1,2,3,4]
# [j,k,l,m] = myNumbers1
# print(F"k: {k}")

# dist
# myObject = dict({'a':232, 'b':433, 'c':435, 'd':533 })
#   myObject
# [v,x,y,z] = myObject
# print(a,b,c,d)
# print(v, x, y, z)

studentInfo = {
    'name': "",
    'lastname': "",
    'age': "",
    'phone': ''
}

class Student:
    def __init__(self, name):
        self.name = name
    
    def display(self, **props):
        print(self.name)
        print(props)


student1 = Student("Bhargav")
student1.display(lastname="T", phone=4353, age=26)
student1.display(**{'lastname': "REDD", 'phone':674574, 'age':46})

def update_user(name, **user): # values come with object/ dictionary like {'name':'Me', 'age':9}
    print(user)
    print(name)
    print(user["age"])

update_user("Me", age=9, address="here only") # arguments with keys
update_user(**{'age':9, 'address':"here only", 'name':"Me"})



