
#list
L = [x*x for x in range(10)]

#generator
L1 = (x*x for x in range(10))

def p(l):
	for n in l:
		print(n)




def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield a
		a, b = b, a + b
		n = n + 1
	return 'done'



def odd():
	print('step 1')
	print('step 2')
	print('step 3')
	yield 1

next(odd)
for i in odd:
	pass