a = "sofadsrinivas"
vowel="aeiou"

#for i in a:
#	print(i)

i=0
while (i < len (a)):
#	print(a[i])
	if (a[i] in vowel):
		print('vowel has reached "',a[i],'"')
		i += 1
		pass
		#continue
		#break
	print(a[i])
	i += 1

