def get_primes(n: int) -> set:
    sieve = n * [True]
    sieve[0] = sieve[1] = False
    for i in range(2, len(sieve)):
        if sieve[i]:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = False

    res = []
    for i, prime in enumerate(sieve):
        if prime:
            res.append(i)
    return res


def fast_pow(base, exp, mod):
    res = 1
    pot = base % mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * pot) % mod
        exp >>= 1
        pot = (pot * pot) % mod
    return res


bound = 1000000
primes = get_primes(bound)
for i, p in enumerate(primes):
    p2 = p * p
    x = (fast_pow(p - 1, i + 1, p2) + fast_pow(p + 1, i + 1, p2)) % p2
    if x > 10 ** 10:
        print(i + 1)
        break
