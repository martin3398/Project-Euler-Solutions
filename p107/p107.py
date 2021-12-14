def parse_input(parsed_lines: list[str]) -> (list, dict):
    sorted_list = []
    adjacent_list = {}
    for (i1, e) in enumerate(parsed_lines):
        split = e.strip().split(',')
        for (i2, x) in enumerate(split):
            if x != '-':
                if (i2, i1, int(x)) not in sorted_list:
                    sorted_list.append((i1, i2, int(x)))
                    if i1 in adjacent_list:
                        adjacent_list[i1].append(i2)
                    else:
                        adjacent_list[i1] = [i2]
                    if i2 in adjacent_list:
                        adjacent_list[i2].append(i1)
                    else:
                        adjacent_list[i2] = [i1]

    return sorted(sorted_list, key=lambda d: d[2], reverse=True), adjacent_list


def is_connected(contained, adj_list):
    marked = set()
    queue = [0]
    while queue:
        next_val = queue.pop()
        if next_val not in marked:
            marked.add(next_val)
            queue.extend(adj_list[next_val])

    return marked == set(contained)


if __name__ == '__main__':
    with open('input.txt') as file:
        lines = file.readlines()

    if lines:
        res = 0
        edge_list, adj_list = parse_input(lines)
        for (i1, i2, weight) in edge_list:
            adj_list[i1].remove(i2)
            adj_list[i2].remove(i1)
            if not is_connected(range(40), adj_list):
                adj_list[i1].append(i2)
                adj_list[i2].append(i1)
            else:
                res += weight
        print(res)
