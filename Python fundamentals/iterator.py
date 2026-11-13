#iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
#Collections are iterable objects which have  a iter() method which is used to get an iterator

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit)) #Same as for loop