import random
'''
#print(dir(random))
a=random.random()
print(a)
a=random.uniform(3,10)
print(a)
a=random.randint(3,10)
print(a)
a=random.randrange(3,10)
print(a)
random.seed(2)
a=random.randint(3,10)
print(a)

l=[2,4,3,1,5]
random.shuffle(l)
print(l)

'''

ml=list(range(100))
print(ml)
random.shuffle(ml)
print(ml)

print(random.choice(ml))
