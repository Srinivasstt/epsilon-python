def getpincode(addr):
	words=addr.split()
	for word in words:
		word=word.strip(",./t")
		if word.isnumeric():
			if(len(word)== 6):
				pincode=word
	return pincode

