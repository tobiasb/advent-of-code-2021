vents = []
max_x, max_y = 0, 0
with open('05_puzzle_input.txt', 'r') as f:
    for line in f.readlines():
        coords = line.strip().split(' -> ')
        vents.append([])
        for i in range(0, 2):
            x, y = [int(val) for val in coords[i].split(',')]
            vents[-1].append((x, y))
            max_x, max_y = max(max_x, x), max(max_y, y)

print(vents)
print(f"Max: x={max_x} y={max_y}")

board = [[0 for _ in range(0, max_x + 1)] for _ in range(0, max_y + 1)]

for row in board:
    print(row)

ignore_diagonal = False
for vent in vents:  # e.g. [(0, 9), (5, 9)]
    print(vent)
    if ignore_diagonal and not (vent[0][0] == vent[1][0] or vent[0][1] == vent[1][1]):
        print(f"Ignoring vent {vent}")
        continue  # Ignore non horizontal or vertical lines

    x, x_end = vent[0][0], vent[1][0]
    y, y_end = vent[0][1], vent[1][1]
    inc_x = 1 if x < x_end else (-1 if x > x_end else 0)
    inc_y = 1 if y < y_end else (-1 if y > y_end else 0)
    print(f'Change: x={inc_x} y={inc_y}')
    while x != x_end or y != y_end:
        print(f"Marking x={x} y={y}")
        board[y][x] += 1

        x += inc_x
        y += inc_y

    print(f"Marking x={x} y={y}")
    board[y][x] += 1

for row in board:
    print(row)

count = 0
for row in board:
    for cell in row:
        count += 1 if cell > 1 else 0

print(count)
