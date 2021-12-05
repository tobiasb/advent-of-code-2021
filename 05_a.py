vents = []
max_x, max_y = 0, 0
with open('05_test_input.txt', 'r') as f:
    for line in f.readlines():
        coords = line.strip().split(' -> ')
        vents.append([])
        for i in range(0,2):
            x, y = [ int(val) for val in coords[i].split(',') ]
            vents[-1].append((x,y)) 
            max_x, max_y = max(max_x, x), max(max_y, y)

print(vents)

board = [ [ 0 for _ in range(0, max_x + 1)] for _ in range(0, max_y + 1) ]
for vent in vents:
    if not vent[0][0] == vent[1][0] or vent[0][1] == vent[1][1]:
        continue # Ignore non horizontal or vertical lines

    for x in range(min(vent[0][0], vent[1][0]), max(vent[0][0], vent[1][0])):
        for y in range(min(vent[0][1], vent[1][1]), max(vent[0][1], vent[1][1])):
            board[y][x] += 1

for row in range(len(board)-1, -1, -1):
    print(board[row])
