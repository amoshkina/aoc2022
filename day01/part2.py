def solve():
    elves = []
    current_elf = 0
    with open('input.txt') as fd:
        
        for line in fd.readlines():
            if line == '\n':
                elves.append(current_elf)
                current_elf = 0
                continue
            current_elf += int(line.strip())
    elves.sort(reverse=True)
    return sum(elves[0:3])

if __name__ == '__main__':
    print('result: ', solve())