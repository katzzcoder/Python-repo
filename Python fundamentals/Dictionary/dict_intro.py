#no duplicate keys allowed. can be accessed via keys.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["model"])
print(thisdict.get("model")) #same as above

#dict constructor
thisdict1 = dict(name = "John", age = 36, country = "Norway")
print(thisdict1)
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
thisdict["year"] = 2000 #update
print(thisdict.items())
thisdict["color"] ="red" #add if missing while accessing
print(thisdict.items())

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") #Checking if key is present

  thisdict.update({"year": 2020})
  print(thisdict)
  thisdict.update({"miles": "new"}) #Adds if missing
  print(thisdict)

  #Remove
thisdict.pop("model")
print(thisdict)
thisdict.popitem() #Removes last item.pop(key) also works 
print(thisdict)
del thisdict["year"] #Gives error if missing


#Looping
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in mydict:
  print(x) #Prints keys in newline. We can also use  for x in mydict.keys():   print(x)
  print(mydict[x]) #Prints values in newline for x in mydict.values():  print(x)

  for x, y in mydict.items():
    print(x, y) #prints both

    x = mydict.setdefault("model", "Bronco")
