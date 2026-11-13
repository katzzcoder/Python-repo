#A decorator is a function that takes another function as input and returns a new function.

def changecase(func):
  def myinner():
    print("control2")
    return func().upper()
  print("control1")   
  return myinner

@changecase
def myfunction():
  print("control3")
  return "Hello Sally"

print(myfunction())

#*args and **kwargs

def changecase1(func):
  def myinner(*args, **kwargs):
    print("2- control")
    return func(*args, **kwargs).upper()
  print("1- control")
  return myinner

@changecase1
def myfunction(nam):
  print("3- control")
  return "Hello " + nam

print(myfunction("John"))
print(myfunction.__name__) #This returns inner function myinner

#Function metadata: __name__ returns name of the function
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

import functools

def changecase(func):
  @functools.wraps(func) #This will preserve actual function detail
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)