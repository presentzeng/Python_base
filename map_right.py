from functools import reduce

L = ['adam', "LISA", "barT"]

def fn(name_list):
		return (name_list.capitalize())

a = list(map(fn, L))
#a = list(fn(L))
#print(fn(L))
print(a)

