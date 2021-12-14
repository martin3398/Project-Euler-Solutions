from sympy import totient

if __name__ == '__main__':
    res = 0
    for i in range(2, 1000000 + 1):
        res += totient(i)
    print(res)
