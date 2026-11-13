def my_func():
    print("hi from function")
my_func()  

#Return
def my_func1():
    return "hi from function"
print(my_func1() ) 

#Arguments and parameneters. Arguments must be in order,also called position arguments
def add(a,b): #a and b are parameters
    return a+b
print(add(6,3)) #6 and 3 are argumets

#Default parameters
def add1(a,b=3): #3 is default value to b
    return a+b
print(add1(6)) # b value sent will override default value

#Keyword Arguments : send exact values from passing then don't need to worry about order

def full_name(firstname,lastname):
    return (firstname,lastname)
print(full_name(lastname ="Thakur" , firstname="kavita"))

#Any type of datatype can be sent to function

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"] #list
my_function(my_fruits)

my_foods = ('burger','pizza') #tuple
my_function(my_foods)

my_string = "I am kavita"
my_function(my_string)

#Function can return anytype of data.




