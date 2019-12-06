from functools import reduce


def valid_password(password: int):
    first = len(str(password)) == 6
    if not first:
        return False
    second = 152085 <= int(password) <= 670283
    if not second:
        return False
    third = reduce(lambda x, y: x or y, [str(password)[i] == str(password)[i + 1] for i in range(len(str(password)) - 1)])
    if not third:
        return False
    fourth = reduce(lambda x, y: x and y, [int(str(password)[i]) <= int(str(password)[i + 1]) for i in range(len(str(password)) - 1)])
    if not fourth:
        return False
    return first and second and third and fourth


def part_2_valid(password: int):
    s_password = str(password)

    for digit in s_password:
        if s_password.count(digit) == 2:
            return True

    return False


if __name__ == "__main__":

    # Part 1
    xs = []

    for x in range(152085, 670284):
        if valid_password(x):
            xs.append(x)
    print("Answer 1:", len(xs))

    # Part 2
    ys = []

    for x in xs:
        if part_2_valid(x):
            ys.append(x)

    print("Answer 2:", len(ys))
