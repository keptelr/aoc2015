import utils

vowels = "aeiouAEIOU"
bad_substrings = ["ab", "cd", "pq", "xy"]


def part1(input: str):
    count = 0
    for line in input.split("\n"):
        if nice(line) is True:
            count += 1
    return count


def count_vowels(input: str) -> int:
    num_vowels = 0
    for char in input:
        if char in vowels:
            num_vowels = num_vowels+1
    return num_vowels


def contain_twice_letters(input: str) -> bool:
    last_char = ""
    for char in input:
        if char is last_char:
            return True
        else:
            last_char = char
    return False


def contain_bad_substings(input: str) -> bool:
    for bad_substring in bad_substrings:
        if bad_substring in input:
            return True
    return False


def part2():
    # TODO
    None


def nice(input: str) -> bool:
    return (count_vowels(input) >= 3) and (contain_twice_letters(input)) and not (contain_bad_substings(input))


if __name__ == '__main__':
    input = utils.read("day05")
    print(part1(input))
    # print(part2(input))
