from math import log


lines = None
with open('p099_base_exp.txt', 'r') as f:
	lines = f.readlines() 

max_val = 0
max_index = -1

if lines is not None:
	for i, e in enumerate(lines):
		split = e.strip().split(',')
		val = int(split[1])*log(int(split[0]))
		if val > max_val:
			max_val = val
			max_index = i

print(max_index + 1)
