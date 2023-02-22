# objects with countable number of values
# any object that can be trasversed
# any object that implements the iterator protocol : __iter__() and _next_()

# iterator vs iterables :iterables( lists sets dictionaries tuples etc) all have method iter()
# iter() method enables objects to be trasversed or looped
mytuple = ("1", "2", 3)
myiterable = iter(mytuple)
# access to the next
print(next(myiterable))
print(next(myiterable))
print(next(myiterable))

x = ("hanks")
myiterable=iter(x)
print(next(myiterable))

