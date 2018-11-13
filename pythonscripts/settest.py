setA = {2,4,5,7,43,54,3}
setB = {3,4,2,5}

for i in setA:
	print(i)
for i in setB:
	print(i)

print(setA.intersection(setB))
print(setA.union(setB))

print(setA - setB)
