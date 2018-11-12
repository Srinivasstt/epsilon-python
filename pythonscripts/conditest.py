'''
a = "z"

if (a == "z"):
	print("a is z")
	print("still in if block")
print ("out of if block")
'''
s = "aeifodugsiovlwevuioae"
vowel = "aeiou"

if (s[0] in vowel):
	print(s[0],": 1st leter is vowel")
elif (s[0].isdigit()):
	print(s[0]," is digit")
else:
	print(s[0],": is not vowel or digit")

print ("out of if block")


