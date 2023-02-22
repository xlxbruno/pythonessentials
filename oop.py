# object and classes
# OBJECT ORIENTED PROGRAMMING (OOP) # we should treat our programs with a level of abstarction, reusability
# a class is a blueprint for an object
# we use class keyword for creation

class testclass:
    x = 10  #variables in classes are properties

# objects are a collection of classes
# to createobject reference the class on  a call
object1 = testclass()
print(object1.x)


# in oop classes define the properties and methods that work on those properties
# eg. Vehicle : 4 seats, engine, color, speed
# we haave a function called init that defines info about an object created from a set blueprint
# self in classes points to the object being created

class Student:

    def  __init__(self, name, age, unit, doa):
        self.name = name
        self.age = age
        self.unit = unit
        self.doa = doa


    def greetstudent(self):

        other = "!"
        print("hello " + self.name + other)

# create the objects with initialized values
student1 = Student("Hanks", "18" ,"f4", "monday")
student2 = Student("Bruno", "17" ,"f3", "sunday")

print(student1.name)
student1.greetstudent()
student2.greetstudent()
