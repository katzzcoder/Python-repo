# Can be used any iterable

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set0 = {4,5,6}
set5 = {"b",2,7,9}

#union , can use |
set3 = set1.union(set2)
print(set3)
set4 =set1.union(set2,set0) # or use set1|set2|set0
print(set4)

# intersection or &
set6 = set1.intersection(set5)
print(set6)

#intersection_update -keeps only duplicates
#The difference() method will return a new set that will contain set1-set2
#difference_update() -same as difference but it changes original set
#The symmetric_difference() opposite of intersection
#symmetric_difference_update()-same but makes change in original set

#Frozenset - immutable
	
#isdisjoint()	 	Returns True if there is NO intersection between two frozensets	
#issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
#issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	

