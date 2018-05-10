#sorted

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return sorted(t, key=lambda t:t[1])

print(by_name(L))