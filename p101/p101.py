import numpy as np
from numpy.polynomial import Polynomial

if __name__ == '__main__':
    error_sum = 0
    poly = Polynomial([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])
    values = np.array([poly(x) for x in range(1, 12)])
    for i in range(10):
        fitted_poly = np.poly1d(np.polyfit(range(1, i + 2), values[:i+1], deg=i))
        calculated = np.array([fitted_poly(x) for x in range(1, 12)])
        error_sum += np.round(calculated[i + 1])
    print(int(error_sum))
