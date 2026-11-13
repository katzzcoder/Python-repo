a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#shoerthand
x="kavita"
y ="Thakur"
if "a" in x: print(f"i am {x}")  
print(f"i am {x}") if "T" not in y else print(f"i am {y}")

#assignment
a=100
b=50
bigger = a if a>b else b
print(f"bigger number is {bigger}")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#pass
age = 20
if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

#match -If you have so many conditions
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")  
 #Combining cases
day = "Sat"
match day:
     case "Mon"|"Tue"|"Wed"|"Thu"|"Fri":
        print("weekday")
     case "Sat"|"Sun" :
        print("Weekend")  
     case _:
        print("Wrong entry")
   
