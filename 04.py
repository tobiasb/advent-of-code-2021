numbers = []
cards = []

with open('04_puzzle_input.txt', 'r') as f:
    numbers = f.readline().strip().split(',')
    print(numbers)

    f.readline()

    while True:
        card = []
        for _ in range(0, 5):
            card.append(f.readline().strip().replace('  ', ' ').split(' '))

        print(card)
        cards.append(card)
        if not f.readline():
            break

cards_done = []

winner = False
for picked_val in numbers:
    for card in cards:
        for row in card:
            # mark number
            for i, cell_val in enumerate(row):
                if picked_val == cell_val:
                    row[i] = 'x'

        if card in cards_done:
            continue

        winner = False
        # check rows
        for row in card:
            if ''.join(row) == len(row) * 'x':
                winner = True
        # check columns
        for y in range(0, len(card[0])):
            if ''.join([row[y] for row in card]) == len(card[0]) * 'x':
                winner = True

        if winner:
            print('we got a winner')
            unmarked = 0
            for row in card:
                print(row)
                unmarked += sum([int(val) for val in row if val != 'x'])
            print(f'Sum unmarked: {unmarked}, last number: {picked_val}')
            print(unmarked * int(picked_val))
            cards_done.append(card)

        if len(cards_done) == len(cards):
            exit
