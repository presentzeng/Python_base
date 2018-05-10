import math
# Null func
def nop():
	pass

# parameter check
def my_int_check(x):
	if not isinstance(x, (int)):
		raise TypeError('not int')

# return multi val return tuple
def test_return(x, y, z):
	return x+y, x+z

a,b = test_return(1, 2, 3)
print(a, b)

# practice
def qua(a, b, c):
	pass