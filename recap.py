# Function is a block of organized and reusable code that is used to perform a single related action
# How to define a function
# 1. Are defined using keyword def
# 2. Followed by function name
# 3. Followed by paranthesis ():
# 4. eg def checkout()
# 5. Function need to be called for them to be executed
# 6. to call a function we use the name of the function with a set of paranthesis

def greeting():
    # write the code logic / block of code function should run
    # to end a function use return keyword
    data = "hi there from checkout"
    return data


greeting()  # to call a function

# 7. Function here have parameters , parameters are info that a function need in code execution
# to define a function with parameters add the parameters in the paranthesis are variables
# in above example if greeting comes from user then the definition will look like this:

message = "Hello from user"


def greeting_from_user(greet):  # here greet is parameter
    print(greet)
    return


greeting_from_user(message)  # here message is arguement


def simple_add(num1, num2):
    print(int(num1) + int(num2))
    return


simple_add(10, 3)

# default arguements : when u initialize parameters with default values


def default_arguments(num1, num2=2):
    d_ivision = (int(num1) / int(num2))
    print(int(d_ivision))
    return


default_arguments(30, 10)

# SCOPE OF VARIABLES IN A FUNCTION
# to basic scopes of variables in python : global and local
# global are defined outside functions and can be accessed by all the files in the scope
# local variables are defined within functions and can only be accessed in the function that defines them
# local can be made accessible to other functions by passing them as arguements to the other functions
# the other functions should accept parameters and the call to those functions should be made in the function
# that define
# the local variable

result = 0  # is global variable
message_local = "version no: "


def s_um(num1, num2):
    message_local = "result is "
    result = num1 + num2  # is local
    print(message_local + str(result))
    return


def division(num1, num2):
    result = num1 / num2  # is local
    print(message_local + str(result))
    return


s_um(10, 10)
division(100, 10)

# ANONYMOUS FUNCTIONS
# not declared using def keyword
# created using the lamda keyword
# can take a number of arguements but can only return one value in expression form
# we cant use print directly in writing them
# can only access global variables and listed parameters

# lambda [arg, arg, arg] : expression  # simmple syntax
# to work with them well , store the lambda function inside a variable

s_um = lambda num1, num2: num1 + num2
print("value of " + str(s_um(20, 10)))

# EXE:PLACE CLUB PROGRAM CODE IN FUNCTIONS

def checkin(age, sex):
    if age > 18:
        if sex == "Male":
         print("Can enter but no free drink")
        else:
         print("Can enter plus free drink,its ladies night")
    elif age < 18 and age > 0:
        print("Too young to drink")
    else:
        print("Invalid input")

    return

checkin(18, "female")








# Tuples allow us to store multiple items in one variable
# are ordered and unchangeable
# defined with ()
shoppingTuple = ("Bread", "Sugar", "Salt", "Bread", "Sugar")
print(shoppingTuple)
# are indexed
# allow duplicates
# to get length use len()
print(len(shoppingTuple))
# tuple with one item
tupleOne = ("Bread",)
# can havee same or diff datat types
tuple1 = (1, 3 ,45, 5)
tuple2 = (1, True, False, "Another string")

type(tuple1)
print(type(tuple2))

# accessing a tuple : by ref index number
print(shoppingTuple[0])
print(shoppingTuple[-1])
print(shoppingTuple[2:5])
print(shoppingTuple[1:])
print(shoppingTuple[:5])
print(shoppingTuple[-1:-4])

# checking if items exist
search = "salt"
if search in shoppingTuple:
    print("yes " + search + " in basket")
else:
    print("No " + search + " in basket")



# loop concept

start = 1
while start < 100:
    print(start)
    start += 1
    if start < 110:
        continue
    else:
        print("End")


fruits = ["Grapes", "Oranges", "Banana"]
fruitsTuple = ("Mango", "Avocado", "Pineapple")

for x in fruits:
    if x == "Grapes":
        print("I have " + x)
    else:
        print(x)



for y in fruitsTuple:
    print(y)



for x in range(10, 20 ,8):
    print("Last loop " + str(x))



loop1 = ["a", "b", "c"]
loop2 = ["e","f", "g"]

for x in loop1:
    for y in loop2:
        print(x, y)

empty = ""
for x in (1, 2, 3):
    pass






