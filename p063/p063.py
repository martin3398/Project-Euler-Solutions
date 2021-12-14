if __name__ == "__main__":
    i = 0
    nums = set()
    # we can exclude base >= 10
    for base in range(1, 10):
        num = 1
        # the growth is too fast for exponents roughly > 200
        for exponent in range(1, 200):
            num *= base
            if len(str(num)) == exponent:
                nums.add(num)
                # print(str(base) + " ** " + str(exponent) + ": " + str(num))
                i += 1

    print(i)
