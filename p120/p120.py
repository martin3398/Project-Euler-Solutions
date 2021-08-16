res = 0

min_bound = 3
max_bound = 1000
for a in range(min_bound, max_bound + 1):
	# algebraic maximum
	n = (a - 1)//2
	# (a-1)^n + (a+1)^n mod a^2 = 2an
	res += (2*a*n)

print(res)
