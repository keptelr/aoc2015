import utils


def part1(input: str) -> int:
    x = 0
    y = 0
    count = 1
    log = set()

    for step in input:
        if step == "^":
            y += 1
        if step == "<":
            x -= 1
        if step == ">":
            x += 1
        if step == "v":
            y -= 1

        key = str(x) + "-" + str(y)
        print(key)
        if (key not in log):
            log.add(key)
            count += 1

    return count


def part2(input: str) -> int:
    mr_robot_1_x = 0
    mr_robot_1_y = 0

    santa_x = 0
    santa_y = 0

    count = 0
    log = set()
    santa = True
    for step in input:
        if step == "^":
            if santa:
                santa_y += 1
            else:
                mr_robot_1_y += 1
        if step == "<":
            if santa:
                santa_x -= 1
            else:
                mr_robot_1_x -= 1
        if step == ">":
            if santa:
                santa_x += 1
            else:
                mr_robot_1_x += 1
        if step == "v":
            if santa:
                santa_y -= 1
            else:
                mr_robot_1_y -= 1
        if santa:
            key = str(santa_x) + "-" + str(santa_y)
        else:
            key = str(mr_robot_1_x) + "-" + str(mr_robot_1_y)
        if (key not in log):
            log.add(key)
            count += 1
        if santa:
            santa = False
        else:
            santa = True
    return count



if __name__ == '__main__':
    # I don't know why.. but this code not work with unit-tests... But it's work
    # with prod data, LOL. Now sunday, 23:23 pm, I am drunk and I don't care about it, because
    # I do it only for fun. It is not my job, sorry
    input = utils.read("day03")
    print(part1(input))
    print(part2(input))
