#slice
L = ['a', 'b', 'c', 'd']

a = L[0:3]

def test():
	if L[0] == 'a':
		print(1)
	else:
		print(2)

#enumerate

def func():
	for i in enumerate(L):
		print (i)


# find min&max
L1 = [3, 2 ,7 ,5 ,6]
def find_max(L):
	min = L[0]
	max = L[0]
	for i in L:
		if i < min:
			min = i
		if i > max:
			max = i
	return (min, max)

a = find_max(L1)
print(a)



