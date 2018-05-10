
#generator
L = []
for x in range(1, 11):
	L.append(x*x)

#print(L)

L1 = [x*x for x in range(1, 11)]

L2 = [x*x for x in range(1, 11) if x%2 == 0]

L3 = ['Hello', 'world', 18, 'Apple', None]

def fi(L):
	tmp = []
	for i in L:
		if isinstance(i, str):
			tmp.append(i)
	return tmp

a = fi(L3)
print(a)

