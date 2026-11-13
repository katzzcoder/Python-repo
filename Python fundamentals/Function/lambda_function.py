#small anonymous function.A lambda function can take any number of arguments, but can only have one expression.

from ast import Lambda


x = lambda a,b:a*b
print(x(5,6))

#Lambda functions used as anonymous function within a function. 
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
#Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
#Using Lambda with map()    
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#Using Lambda with filter()
moldulus = list(filter(lambda x: x % 2==0, numbers))
print(moldulus)

#Using Lambda with sorted(): Can use lambda as key

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)