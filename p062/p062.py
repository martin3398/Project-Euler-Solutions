from collections import Counter

if __name__ == '__main__':
    max_perms = []
    search_max = 100
    while True:
        cubes = [x ** 3 for x in range(search_max)]
        cubes_sorted = ["".join(sorted(str(x))) for x in cubes]
        most_common = Counter(cubes_sorted).most_common(1)
        if len(most_common) > 0 and most_common[0][1] == 5:
            max_perms = most_common
            break
        else:
            search_max += 100
    max_perms = [x[0] for x in max_perms]
    candidates = [x for x in cubes if "".join(sorted(str(x))) in max_perms]
    print(min(candidates))
