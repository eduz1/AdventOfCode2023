# Add more spaces depending on whats needed on the operations
def update_map_len(map, line_op):
    op_len = line_op[2]
    map_len = len(map)

    if line_op[0] >= line_op[1]:
        op_len += line_op[0]
    else:
        op_len += line_op[1]

    if map_len < op_len:
        for x in range(map_len, op_len):
            map.append(x)

    return map

def update_map_op(map, line_op):
    rem = []
    dest = line_op[0]
    source = line_op[1]
    op_len = line_op[2]

    rem = map[dest : dest + op_len]
    print(rem)
    print()
    map[dest : source] = map[dest + op_len : source + op_len]
    map[source : source + op_len] = rem

    print(map)
    print()

    return map

if __name__ == "__main__":
    seeds = []
    seed_map = []
    section = 0
    next_line = 0

    f = open("test.txt", "r")

    seeds = [int(num) for num in f.readline().split() if num.isdigit()]

    for line in f:
        line = line[:-1]
        if ":" not in line:
            if len(line) > 0:
                seed_op = [int(num) for num in line.split() if num.isdigit()]
                update_map_len(seed_map, seed_op)
                update_map_op(seed_map, seed_op)

    for i in seeds:
        print(seed_map[i - 1])
