import utils

def part1(input: str) -> int:
    floor = 0
    for char in input:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

    return floor

def part2(input: str) -> int:
    floor = 0
    for i in range(0, len(input)):
        if input[i] == "(":
            floor += 1
        elif input[i] == ")":
            floor -= 1
        if floor == -1:
            return i + 1

if __name__ == '__main__':
    input = utils.read("day01")
    print(part1(input))
    print(part2(input))
