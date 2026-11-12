# Ordered ,changeable and allow duplicates
x =[1,2,"red",True]
print("showing list x:", x,"\nLength of x:", len(x))

#List costructor
mylist = list((1,2,3)) #double parenthesis
print(mylist)
#access item
print(mylist[1],mylist[-1])

#Changing list items:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert() , append and extend
thislist1 = ["apple", "banana", "cherry"]
thislist1.insert(2, "watermelon") #Insert on index
print(thislist1)
thislist1.append("orange") #Append at end
print(thislist1)
thislist2 =[1,2,3]
thislist1.extend(thislist2)
print(thislist1)

#remove , pop, del and clear
thislist1.remove("apple")
print(thislist1)
thislist1.pop()
print(thislist1)
thislist1.pop(1)
print(thislist1)
del thislist1[1]
print(thislist1)

thislist1.clear()
print(thislist1)
del thislist1
#print(thislist1) will show error now as list not available anymore
