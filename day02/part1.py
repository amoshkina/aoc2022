SOLE_SCORER = {
    # 'A': 1,
    # 'B': 2,
    # 'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

PAIR_SCORER = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3
}


def solve():
    my_score = 0
    with open('input.txt') as fd:
        for line in fd.readlines():
            opponent, me = line.strip().split(' ')
            my_score += SOLE_SCORER[me]
            my_score += PAIR_SCORER[opponent+me]

    return my_score
            

if __name__ == '__main__':
    print('result: ', solve())