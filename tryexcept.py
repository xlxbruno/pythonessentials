# called try except else finally
# try lets u test a block of code for errors
# except lets u handle errors
# else : when no error executes the code
# finally : runs code regardless of errors

# Exception Handling
x = -2
try:
    print(x)
except:
    print("An error occured, check if email is defined")
else:
    print(str(x) + " from else statement")
finally:
    print("enter x")


# raise keyword : works on condition, if condition is met raise an error message/exception
if x < 0:
    # raise Exception("Should not be less than zero")
    raise TypeError("should x not be less")
