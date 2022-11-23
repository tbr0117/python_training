## for <condition/ expression>:

for number in range(3):
    print("iteration", number, (number + 1) * ".")
#
times = int(input("times: "))

for number in range(1, times, 2):
    print("iteration for 2: ", number, number * ".")

## break loop

sucessfull = True
for number in range(3):
    # For loop block
    print("Attempt", number + 1)
    if sucessfull:
    # if block start
        print("Successfull")
        break # end/ exit loop


## for / else
## for loop have "else" block and it's will trigger if loop end with out "break" statement

sucessfull = False

for number in range(3):
    # For loop block
    print("Attempt", number + 1)
    if sucessfull:
    # if block start
        print("Successfull")
        break # end/ exit loop
else:
# else of "for" loop
    print("all attempts are failed")



## Nested Loops
for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")


## Iterables
# range -  for x in range(3):
# string - for y in "Python":
# list - foz z in [1,2,3,4]:


## while loop

number = 100
while number > 0:
    print("number", number)
    number //= 2 # number = number // 2

command = ""

while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)


## Infinity Loop

command = ""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
