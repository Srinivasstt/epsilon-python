addr={"fname":"srini","lname":"vas"}
print(addr["lname"])
print(addr.keys())
print(addr.values())
print(list(addr.items()))
print(list(addr.keys()))
#addr["pincode"]=["560037"]
#print(addr)
'''
addr2={"name":{"fname":"vas","lname":"srini"}}
print(addr2["name"])
print(addr2["name"]["fname"])
'''

for k,v in addr.items():
	print(k + v)
