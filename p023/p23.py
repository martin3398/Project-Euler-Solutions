import numpy as np

def get_divisors(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i


upper_bound = 28123

abundant = set()

for i in range(12, upper_bound + 1):
	if sum(get_divisors(i)) > i:
		abundant.add(i)

#print('creating abundant set done')


l = np.zeros(upper_bound + 1, dtype=bool)
for i in abundant:
	for j in abundant:
		if i + j <= upper_bound:
			l[i + j] = True

res = 0
for i in range(len(l)):
	if not l[i]:
		res += i

print(res)
