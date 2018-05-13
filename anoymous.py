# anonymous func
import functools
import sys 

L1 = list(map(lambda x: x*x, [1, 2, 3 ,4]))
print(L1)

#partial
int2 = functools.partial(int, base = 2)
p = int2('10000')

max2 = functools.partial(max, 10)
p2 = max2(5, 6, 7)

#sys
def test():
	args = sys.argv
	if len(args) == 1:
		print('hello world')
	elif len(args) == 2:
		print('hello %s world' % args[1])
	else:
		print('too many arguments')


def func(x):
	sum = 20000
	i = 1
	while i < x:
		sum = (sum + 20000) *1.12 
		i = i + 1
	return sum

print(func(5))