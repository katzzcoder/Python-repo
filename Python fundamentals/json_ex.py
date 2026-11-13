#Convert from JSON to Python:
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y =json.loads(x)
print(y)
print(y["name"])

#Convert from Python to JSON

mydict =  { "name":"John", "age":30, "city":"New York"}
myjson =json.dumps(mydict)
print(myjson) 
print(myjson[0:10]) #reads as string