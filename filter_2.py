#filter

def odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def fil(n):
	tmp = str(n)	
	l = len(tmp)//2
	i = 0
	while i < l:
		if tmp[i] == tmp[-1 - i]:
			i = i + 1
			continue
		else:
			break
	if i == l:
		print('ok')
	else:
		print('fail')


a = fil(123211)
print(a)






