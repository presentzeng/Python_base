from functools import reduce

def fn(x, y):
	return x + y

a = reduce(fn, [1, 2, 3])
print(a)

