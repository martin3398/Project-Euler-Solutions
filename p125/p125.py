
def is_palindromic(i):
	return str(i) == str(i)[::-1]

bound = 10000

squares = [a**2 for a in range(1, bound + 1)]

res = set()

for i in range(len(squares)):
	s = squares[i]
	for j in range(i + 1, len(squares)):
		s += squares[j]
		if s >= 10**8:
			break
		elif is_palindromic(s):
			res.add(s)

print(sum(res))
