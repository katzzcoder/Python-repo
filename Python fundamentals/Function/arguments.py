#Positional-Only Arguments. To specify positional-only arguments, add , / after the arguments:
def my_function(name, /):
  print("Hello", name)

my_function("Emil") # name ="Emil" will give error

#Keyword-Only Arguments:To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, name):
  print("Hello", name)
my_function(name = "Emil")

#We can combine both position only and keyword only

#*args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#args* with regular arguments
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

#*Kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#You can combine regular parameters with **kwargs and *args.The order must be:regular parameters, *args and **kwargs

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

#unpacking
#*args
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

#**kwargs
def my_function(fname,lname):
  return ("hello",fname,lname)

person = {"fname":"Emil", "lname" :"Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")