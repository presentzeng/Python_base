from functools import reduce

L = ['adam', "LISA", "barT"]

def fn(name_list):
	for i in name_list:
		return (i.capitalize())

a = list(map(fn, L))
print(a)

