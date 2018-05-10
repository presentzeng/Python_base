# return function

def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1, f2, f3 = count()
print(f1(), f2() ,f3())	

def count1():
	fs = []
	def f(j):
		def g():
			return j*j
		return g
	for i in range(1, 4):
		fs.append(f(i))
	return fs

f1, f2, f3 = count1()
print(f1(), f2() ,f3())	
