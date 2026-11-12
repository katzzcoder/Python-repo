# copy ways
mylist = [1,2,3,4]
copylist = mylist.copy() #via copy
print(mylist)
print(copylist)
copylist1 = mylist[:] #via slicing 
print(copylist1)
copylist2 = list(mylist) #via list constructor
print(copylist2)

#join ways
for x in copylist1:
    copylist.append(x) 
print(copylist) # via append

copylist_concat = print(copylist1+copylist2) #concat
copylist1.extend(copylist2)
print(copylist1) #via extend

copylist3 = copylist*2
print(copylist3)
