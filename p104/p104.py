if __name__ == '__main__':
    fib = 1
    last = 1
    k = 2
    while True:
        last, fib = fib, fib + last
        k += 1
        if set(str(fib % 10**9)) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'} \
                and set(str(fib)[:9]) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            print(k)
            exit(0)
