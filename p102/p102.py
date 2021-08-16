from math import log
import numpy as np

def d(p1, p2):
	return (p1[0]-p2[0])*p2[1]-p2[0]*(p1[1]-p2[1]);


lines = None
with open('p102_triangles.txt', 'r') as f:
	lines = f.readlines() 

if lines is not None:
	arr = np.zeros((len(lines), 3, 2))
	for i, e in enumerate(lines):
		split = e.strip().split(',')
		for j in range(3):
			for k in range(2):
				arr[i, j, k] = int(split[2*j+k])

	res = 0
	for e in arr:
		d1 = d(e[0], e[1])
		d2 = d(e[1], e[2])
		d3 = d(e[2], e[0])
		if (d1 > 0 and d2 > 0 and d3 > 0) or (d1 < 0 and d2 < 0 and d3 < 0):
			res += 1

	print(res)
