#Ordered, unchangeable and allow duplicates
mytuple= ("apple", "banana", "cherry") 

thistuple = "apple", "banana", "cherry" #This is also tuple
print(thistuple)
print(thistuple[1])

#Workaround to change tuple . We can change tuple to list and apply list methods
mylist = list(mytuple)
mylist[1] = "kiwi"
mytuple = tuple(mylist)
print(mytuple)

#Creating tuple with 1 item -add "," at end else it is a string
newtuple =("orange",)
print(newtuple)

#Two tuples can be concatenated
newtuple2 = newtuple+mytuple
print(newtuple2)

# del keyword to delete tuple(we caan't use it on it's items directly as it is unchangeable
del newtuple2
#  print(newtuple2) - not defined error

#Asterik unpacking
food = ("burger","pizza","sandwich","chowmin")
(a,b,*c) = food  #These are variable names
print(c) #* variable will contail all rest of the items
(f,*d,e) =food
print(f,d,e) # d will have all extra items,rest will be assigned with 1 items
