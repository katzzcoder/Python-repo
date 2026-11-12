thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for x in range(len(thislist)):
  print(thislist[x]) #Index, range  and length function to iterate list

i=0
while i < len(thislist):
    print(thislist[i])
    i=i+1

#List Comprehension
fruits = ["watermelon","apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist1 = [x for x in range(10) if x%2==0]
print(newlist1)
newlist2 = [x.upper() for x in fruits]
print(newlist2)
newlist3 =["hello" for x in newlist1] #numeric list changed to all hello
print(newlist3)
list4 = [x if x =="kiwi" else "grapes" for x in fruits]
print(list4)

#sort,reverse
fruits = ["kiwi", "mango","watermelon","apple", "banana", "cherry"]
fruits.sort()
print(fruits)
fruits.sort(reverse =True)
print(fruits)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower) # Sorting lowercase first
print(thislist)
thislist.reverse()
print(thislist)
