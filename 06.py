from multiprocessing import Pool

test_input = [3,4,3,1,2]
puzzle_input = [3,5,3,1,4,4,5,5,2,1,4,3,5,1,3,5,3,2,4,3,5,3,1,1,2,1,4,5,3,1,4,5,4,3,3,4,3,1,1,2,2,4,1,1,4,3,4,4,2,4,3,1,5,1,2,3,2,4,4,1,1,1,3,3,5,1,4,5,5,2,5,3,3,1,1,2,3,3,3,1,4,1,5,1,5,3,3,1,5,3,4,3,1,4,1,1,1,2,1,2,3,2,2,4,3,5,5,4,5,3,1,4,4,2,4,4,5,1,5,3,3,5,5,4,4,1,3,2,3,1,2,4,5,3,3,5,4,1,1,5,2,5,1,5,5,4,1,1,1,1,5,3,3,4,4,2,2,1,5,1,1,1,4,4,2,2,2,2,2,5,5,2,4,4,4,1,2,5,4,5,2,5,4,3,1,1,5,4,5,3,2,3,4,1,4,1,1,3,5,1,2,5,1,1,1,5,1,1,4,2,3,4,1,3,3,2,3,1,1,4,4,3,2,1,2,1,4,2,5,4,2,5,3,2,3,3,4,1,3,5,5,1,3,4,5,1,1,3,1,2,1,1,1,1,5,1,1,2,1,4,5,2,1,5,4,2,2,5,5,1,5,1,2,1,5,2,4,3,2,3,1,1,1,2,3,1,4,3,1,2,3,2,1,3,3,2,1,2,5,2]
own_test_input = [1]

input = [ (ttb, 0) for ttb in puzzle_input ]
days = 256

total_fish = 0

def count_fish(tuple):
    total_fish = 0
    input = [tuple]
    while len(input) > 0:
        print(f'Batch size: {len(input)}')
        total_fish += len(input)
        next_round = []
        for ttb, birth_day in input:
            births = 0
            for day in range (birth_day, days + 1):
                if ((ttb + births * 7) - (day - birth_day)) == 0:
                    if days >= day + 1:
                        births += 1
                        next_round.append((8, day + 1))
        input = next_round
    return total_fish

if __name__ == '__main__':
    with Pool(50) as p:
        fish_counts = p.map(count_fish, input)
        print(f'{sum(fish_counts)} fish total')
