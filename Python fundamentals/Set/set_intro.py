#unordered, mutable and does not allow duplicate
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset) # True and 1 are same for set

#add method insted of append
newset = set(thisset)
print(newset)
thisset.add("orange")
print(thisset)

#set has update method instead of extend
updateset ={1,2,3,4,5}
thisset.update(updateset)
print(thisset)

#Remove and discard. remove gives error if item doesn't exist. pop() removes random item as no indexing in set
thisset.remove("apple")
print(thisset)
#thisset.remove("apple") error
thisset.discard("apple") #No error even though it doesn't exist
