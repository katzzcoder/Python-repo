'''functions that can pause and resume their execution.When a generator function is called, 
it returns a generator object, which is an iterator.The code inside the function is not executed yet,
 it is only compiled. The function only executes when you iterate over the generator.yield keyword makes function generator'''

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

#When yield is encountered, the function's state is saved, and the value is returned. 
# The next time the generator is called, it continues from where it left off.  
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)

def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#When there are no more values to yield, the generator raises a StopIteration exception: