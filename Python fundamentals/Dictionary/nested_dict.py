child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

print(myfamily["child2"]["name"]) #prints Tobias

#Looping
for children, children_details in myfamily.items():
  print(children)

  for detail in children_details:
    print(detail , children_details[detail])

