import sys

def get_digit_1_4_7_8_count(input):
    sum = 0
    for line in input:
        for l in [2, 4, 3, 7]: # 1, 4, 7, 8
            sum += len(list(filter(lambda digit: len(digit) == l, line[1].split(' '))))

    return sum

def get_value(line):
    digits = []

    ref = {
        2: '1',
        4: '4',
        3: '7',
        7: '8'
    }
    
    for digit in line.split(' '):
        digits.append(ref[len(digit)])

    return int("".join(digits))

def get_values_sum(input):
    return sum([ get_value(line) for line in input ])

def get_input_from_file(filename: str):
    input = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            parts = line.split(' | ')
            input.append((parts[0].strip(), parts[1].strip()))
    return input

if __name__ == '__main__':
    input = get_input_from_file(sys.argv[1])
    for line in input:
        print(f"Signal Pattern: {line[0]}")
        print(f"Output values:  {line[1]}")
        print("")
    
    print(f"Count: {get_digit_1_4_7_8_count(input)}")

def test_digit_1_4_7_8_count_with_test_input():
    input = get_input_from_file("08_test_input.txt")
    assert get_digit_1_4_7_8_count(input) == 26

def test_single_values():    
    assert get_value("ab ab ab ab") == 1111
    assert get_value("ba ba ba ba") == 1111
    assert get_value("abcd abcd abcd abcd") == 4444
    assert get_value("dcba dcba dcba dcba") == 4444
    assert get_value("abc abc abc abc") == 7777
    assert get_value("cba cba cba cba") == 7777
    assert get_value("abcdefg abcdefg abcdefg abcdefg") == 8888
    assert get_value("gfedcba abcdefg abcdefg abcdefg") == 8888

# def test_values():    
#     assert get_value("fdgacbe cefdb cefbgd gcbe") == 8394
#     assert get_value("fcgedb cgb dgebacf gc") == 9781
#     assert get_value("cg cg fdcagb cbg") == 1197
#     assert get_value("efabcd cedba gadfec cb") == 9361
#     assert get_value("gecf egdcabf bgf bfgea") == 4873
#     assert get_value("gebdcfa ecba ca fadegcb") == 8418
#     assert get_value("cefg dcbef fcge gbcadfe") == 4548
#     assert get_value("ed bcgafe cdgba cbgef") == 1625
#     assert get_value("gbdfcae bgc cg cgb") == 8717
#     assert get_value("fgae cfgab fg bagce") == 4315


# def test_sum_of_values_with_test_input():
#     input = get_input_from_file("08_test_input.txt")
#     assert get_values_sum(input) == 61229
