import utils


def part1(input: str) -> int:
    final_square = 0
    for line in input.split("\n"):
        parameters = line.split("x")
        length = int(parameters[0])
        width = int(parameters[1])
        height = int(parameters[2])
        square_1 = length * width
        square_2 = width * height
        square_3 = height * length
        final_square += ((2 * square_1) + (2 * square_2) + (2 * square_3) + min(square_1, square_2, square_3))
    return final_square


def part2(input: str) -> int:
    final_square = 0
    for line in input.split("\n"):
        parameters_str = line.split("x")
        parameters_int = sorted(list(map(int, parameters_str)))
        final_square += (parameters_int[0] * 2) + (parameters_int[1] * 2) + (
                    parameters_int[0] * parameters_int[1] * parameters_int[2])

    return final_square


if __name__ == '__main__':
    input = utils.read("day02")
    print(part1(input))
    print(part2(input))
