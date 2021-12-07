import sys

with open(sys.argv[1], 'r') as f:
    pos_x, pos_y = 0, 0

    for line in f.readlines():
        parts = line.strip().split(' ')
        dir, amount = parts[0], int(parts[1])

        if dir == 'up':
            pos_y -= amount
        if dir == 'down':
            pos_y += amount
        if dir == 'forward':
            pos_x += amount

    print(f'Depth: {pos_y}, horizontal position: {pos_x}')
    print(f'Final depth * horizontal position: {pos_y*pos_x}')
