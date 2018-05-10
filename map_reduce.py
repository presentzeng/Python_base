from functools import reduce

x = abs
#print(x(-10))


#input func
def add(x, y, f):
	return f(x) + f(y)

#map
def sqart(x):
	return x*x

L = map(sqart, [1, 2, 3, 4])
print(list(L))

#reduce

def f(x, y):
	return x + y

L1 = reduce(f, [1, 2, 3, 4])
#print(list(L))
print(L1)
