# x power
def power(x, n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s


# default parameter
def power2(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

#a = power2(3)

#changeable parameter
def power3(*x):
	s = 1
	for n in x:
		print(n)


#it will print 2 9
#a = power3(2, 9)

#change list or tuple to changeable parameter
#a = power3(*[2, 9])



