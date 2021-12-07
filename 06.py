from multiprocessing import Pool

test_input = [3,4,3,1,2]
puzzle_input = [3,5,3,1,4,4,5,5,2,1,4,3,5,1,3,5,3,2,4,3,5,3,1,1,2,1,4,5,3,1,4,5,4,3,3,4,3,1,1,2,2,4,1,1,4,3,4,4,2,4,3,1,5,1,2,3,2,4,4,1,1,1,3,3,5,1,4,5,5,2,5,3,3,1,1,2,3,3,3,1,4,1,5,1,5,3,3,1,5,3,4,3,1,4,1,1,1,2,1,2,3,2,2,4,3,5,5,4,5,3,1,4,4,2,4,4,5,1,5,3,3,5,5,4,4,1,3,2,3,1,2,4,5,3,3,5,4,1,1,5,2,5,1,5,5,4,1,1,1,1,5,3,3,4,4,2,2,1,5,1,1,1,4,4,2,2,2,2,2,5,5,2,4,4,4,1,2,5,4,5,2,5,4,3,1,1,5,4,5,3,2,3,4,1,4,1,1,3,5,1,2,5,1,1,1,5,1,1,4,2,3,4,1,3,3,2,3,1,1,4,4,3,2,1,2,1,4,2,5,4,2,5,3,2,3,3,4,1,3,5,5,1,3,4,5,1,1,3,1,2,1,1,1,1,5,1,1,2,1,4,5,2,1,5,4,2,2,5,5,1,5,1,2,1,5,2,4,3,2,3,1,1,1,2,3,1,4,3,1,2,3,2,1,3,3,2,1,2,5,2]
own_test_input = [1]

test_input = [ (ttb, 0) for ttb in test_input ]
puzzle_input = [ (ttb, 0) for ttb in puzzle_input ]

def make_key(ttb, birth_day):
    return f'{ttb}_{birth_day}'

def calc_fish_plus_decendants(ttb, birth_day, days, cache):
    key = make_key(ttb, birth_day)

    if key in cache:
        return cache[key]

    if birth_day > days:
        cache[key] = 0
    else:
        fishes = 0
        for day in range (birth_day, days + 1):
            if ttb == 0:
                fishes += calc_fish_plus_decendants(8, day + 1, days, cache)
                ttb = 7
            ttb -= 1
        
        cache[key] = 1 + fishes
    return cache[key]

def count_fish(input, days):
    cache = {}
    total_fish = 0
    for ttb, birth_day in input:
        total_fish += calc_fish_plus_decendants(ttb, birth_day, days, cache)

    print(f'{total_fish} fish total')
    return total_fish

if __name__ == '__main__':
    count_fish(puzzle_input, 256)

def test_1_0_1():
    assert count_fish([(1, 0)], 1) == 1

def test_2_0_2():
    assert count_fish([(2, 0)], 2) == 1

def test_1_0_2():
    assert count_fish([(1, 0)], 2) == 2

def test_2_0_2():
    assert count_fish([(2, 0)], 2) == 1
    
def test_1_0_10():
    assert count_fish([(1, 0)], 10) == 3

def test_1_0_18():
    assert count_fish([(1, 0)], 18) == 7

def test_test_input_18():
    assert count_fish(test_input, 18) == 26

def test_test_input_80():
    assert count_fish(test_input, 80) == 5934

def test_puzzle_input_80():
    assert count_fish(puzzle_input, 80) == 351092

def test_test_input_256():
    assert count_fish(test_input, 256) == 26984457539