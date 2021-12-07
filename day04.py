import hashlib

def part1(input: str) -> int:
    digest = ""
    number = 0
    while "00000" not in digest[0:5]:
        number += 1
        digest = hashlib.md5((input + str(number)).encode('utf-8')).hexdigest()
    print(digest)
    return number


def part2(input: str) -> int:
    digest = ""
    number = 0
    while "000000" not in digest[0:6]:
        number += 1
        digest = hashlib.md5((input + str(number)).encode('utf-8')).hexdigest()
    print(digest)
    return number

if __name__ == '__main__':
    print(part1("bgvyzdsv"))
    print(part2("bgvyzdsv"))
