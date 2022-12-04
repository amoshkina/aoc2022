def solve():
    max_elf = current_elf = 0
    with open('input.txt') as fd:
        
        for line in fd.readlines():
            if line == '\n':
                max_elf = max(max_elf,  current_elf)
                current_elf = 0
                continue
            current_elf += int(line.strip())

    return max_elf

if __name__ == '__main__':
    print('0000000')
    print('result: ', solve())
