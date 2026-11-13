#try block:test a block of code for errors.
#except block:handle the error.
#else block: execute code when there is no error.
#finally block:execute code, regardless of the result of the try- and except blocks.

try:
  print(x)
except:
  print("An exception occurred")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
#you can choose to throw an exception if a condition occurs.To throw (or raise) an exception, use the raise keyword.

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")