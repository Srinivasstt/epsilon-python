l = [1,2,3,4,34,5,6,9]
l2 = ["a","b","dsd","de","sri","gfr"]
'''
print(l[5])
print(l2[4][1:3])


l2[3] = "ads"
print (l2)


for i in l2:
	if (type(i) == str):
		for j in i :
			print (j)
'''
l.sort()
print(l)
