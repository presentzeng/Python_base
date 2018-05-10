#filter

def is_odd(n):
	return n%2 == 1

L = [1, 2, 3, 4]
a = list(filter(is_odd, L))


def test():
	print('122')
	yield 1
	print(2)

a = test()
#print(a)

def odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

a = odd_iter()
b = next(a)
print(b)
b = next(a)
print(b)

