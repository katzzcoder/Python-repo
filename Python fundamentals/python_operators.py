x = 5
y = 2

print(x % y)
print(x ** y)
print(x // y)

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 4: #count is assigned when if stmt is true
    print(f"List has {count} elements")

    num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday" #Ternary operator

print(x)

x = 5

print(1 < x < 10) #Chaining comparison operator

print(1 < x and x < 10)

#Identity operation is and is not . 
# True only memory of oblect is same but in premitive data type they refer same memory. Use with collections
a = 10
b =10
c =a
x =["red","blue"]
y =["red","blue"]
z =x
print (a is b) #true
print(a is not c) #false
print (x is y) #false
print (z is x) #true

#membership operator
x ="My name is kavita:"

print("name" in x)

