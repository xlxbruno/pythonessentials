# Variables are only avaialable in region created in
# local or global scope
# global scope : outside functions
x = 200  # is accessible in all files
# global keyword : makes variables global
# local scopes are inside functions
# eg, in x an dy below , they are local scopes

def sampleMethod():
    global y
    x = 100
    y = 200
    return x + y

print (sampleMethod())


# what of scopes whan a function is in a function

def sampleFunction():

    def inner_Function():
        print(y)  # inner function ends here, return , print
        return inner_Function()


print(sampleFunction())


# global scope : created outside functions
