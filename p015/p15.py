size = 20

vals = [1]*(size+1)

for i in range(size - 1):
	tmp = vals.copy()
	for i in range(size + 1):
		tmp[i] += sum(vals[:i])
	vals = tmp

print(sum(vals))