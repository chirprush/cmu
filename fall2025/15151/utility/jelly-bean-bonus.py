solvable = {(1, 0), (0, 1)}

N = 20

for n in range(2, N):
    for i in range(0, n + 1):
        state = (i, n - i)

        is_solvable = False

        if state[0] >= 2:
            is_solvable = is_solvable or (state[0] - 2, state[1] + 1) in solvable
        if state[1] >= 2: 
            is_solvable = is_solvable or (state[0] + 1, state[1] - 2) in solvable

        if is_solvable:
            solvable.add(state)

char_map = [[" " for j in range(N)] for i in range(N)]
cmp_map = [[" " for j in range(N)] for i in range(N)]

for s in solvable:
    x = s[0]
    y = N - 1 - s[1]

    char_map[y][x] = "#"

for y in range(N):
    for x in range(N):
        y_ = N - 1 - y

        if (x + 2 * y) % 3 != 0 and x + y < N:
            cmp_map[y_][x] = "#"

for line in char_map:
    print("".join(line))

print()

for line in cmp_map:
    print("".join(line))

