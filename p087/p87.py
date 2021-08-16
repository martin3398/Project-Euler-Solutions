
def get_primes(n: int) -> set:
	sieve = n*[True]
	sieve[0] = sieve[1] = False
	for i in range(2, len(sieve)):
		if sieve[i]:
			for j in range(2*i, len(sieve), i):
				sieve[j] = False

	res = []
	for i, prime in enumerate(sieve):
		if prime:
			res.append(i)
	return res


n = 50000000

primes = get_primes(int(n**0.5) + 1)
res = {0}

for i in range(2, 5):
	res_new = set()
	for x in primes:
		pot = x**i
		if pot >= n:
			break
		for y in res:
			if pot+y < n:
				res_new.add(pot+y)
	res = res_new

print(len(res))
