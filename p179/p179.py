from sympy import divisors

if __name__ == '__main__':
    count = 0
    last = 0
    for i in range(1, 10000001):
        divs = len(divisors(i))
        if divs == last:
            count += 1
        last = divs
    print(count)
