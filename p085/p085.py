if __name__ == '__main__':
    best = 0
    best_num = 0, 0
    for x in range(100):
        for y in range(100):
            num = x * (x + 1) * y * (y + 1) / 4
            if abs(2000000 - num) < abs(2000000 - best):
                best = num
                best_num = x, y
    print(best_num[0] * best_num[1])
