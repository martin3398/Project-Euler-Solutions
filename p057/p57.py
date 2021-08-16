from fractions import Fraction as frac

res = 0
for i in range(1000):
	x = frac(1, 2)

	for j in range(i):
		x = 1/(2+x)

	x += 1
	if len(str(x.numerator)) > len(str(x.denominator)):
		res += 1

print(res)
