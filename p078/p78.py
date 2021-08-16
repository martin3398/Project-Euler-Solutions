
# see also: https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations
# and https://math.berkeley.edu/~mhaiman/math172-spring10/partitions.pdf
def p_list(bound):
	res = [1]
	penta = 1
	for n in range(1, bound):
		p_n = 0
		sign = 1
		for k in range(1, n+1):
			if n - k*(3*k-1)//2 < 0:
				break;
			elif n - k*(3*k+1)//2 < 0:
				p_n += sign*(res[n - k*(3*k-1)//2])
			else:
				p_n += sign*(res[n - k*(3*k-1)//2] + res[n - k*(3*k+1)//2])
			sign *= -1
		res.append(p_n)


	return res

p = p_list(60000)
for (i, num) in enumerate(p):
	if num % 1000000 == 0:
		print(i, num)

