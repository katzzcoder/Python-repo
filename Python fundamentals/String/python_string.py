
#string is array of character
print("kavita")

a="hello" #assigning string to variable
print(a)

b="""my name 
is kavita""" #multiline string
print(b)
print(b[0]) # Access first character

#Looping
for char in b:
    print(char)
#Length of string
print(len(b))

#Check strings using in and not in
print("kavita" not in b) #Returns false
print("kavita" in b) #Returns true

#Check use in coditional statement
if "kavita" not in b:
    print("someone else")
else:
    print("it's kavita")    