from fractions import Fraction as frac

bound = 100

x = frac(1,1) if bound % 3 > 0 else frac((bound//3)*2, 1)
for i in range(bound-1, 1, -1):
	if i % 3 > 0:
		x = 1 + 1/x
	else:
		x = (i//3)*2 + 1/x

x = 2 + 1/x
num = x.numerator
res = sum(int(x) for x in str(num))
print(res)
