def reverse(i):
	return int(str(i)[::-1])


def get_next(i):
	return i + reverse(i)


def is_palindrome(i):
	return str(i) == str(reverse(i))

bound = 10000

non_lychel = set()
num_lychel = 0

for i in range(1, bound + 1):
	intermediates = set()
	cur = get_next(i)
	lychel = True
	for k in range(50):
		intermediates.add(cur)
		if cur in non_lychel or is_palindrome(cur):
			non_lychel |= intermediates
			lychel = False
			break;
		cur = get_next(cur)
	if lychel:
		num_lychel += 1

print(num_lychel)
