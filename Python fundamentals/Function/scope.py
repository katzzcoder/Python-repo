#same variable name inside and outside block - local will override global variable
x = 300

def myfunc():
  x = 200
  print(x)
myfunc()
print(x) #This will give error if no global variable

#If are inside local but need global then use 'global' keyword then you can use it outside of block too

def myfunc3():
  global x
  x = 200
  print(x)
myfunc3()
print(x) 

#This can be used to change the value of variable defined outside block.
x =500
def myfunc4():
  global x
  x = 200
  print(x)
myfunc4()
print(x) #It won't print 500 because value changed in local block.

#Keyword nonlocal: Used in nested block, makes variable belong to outer block.
def myfunc5():
  x = "Jane"
  def myfunc6():
    nonlocal x #Will print Jne if this block not added
    x = "hello"
  myfunc6()
  return x

print(myfunc5())