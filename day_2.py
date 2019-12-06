OP_CODE = [
    1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 19, 10, 23, 1, 23, 13, 27, 1, 6, 27, 31, 1, 9, 31,
    35, 2, 10, 35, 39, 1, 39, 6, 43, 1, 6, 43, 47, 2, 13, 47, 51, 1, 51, 6, 55, 2, 6, 55, 59, 2, 59, 6, 63, 2, 63, 13,
    67, 1, 5, 67, 71, 2, 9, 71, 75, 1, 5, 75, 79, 1, 5, 79, 83, 1, 83, 6, 87, 1, 87, 6, 91, 1, 91, 5, 95, 2, 10, 95, 99,
    1, 5, 99, 103, 1, 10, 103, 107, 1, 107, 9, 111, 2, 111, 10, 115, 1, 115, 9, 119, 1, 13, 119, 123, 1, 123, 9, 127, 1,
    5, 127, 131, 2, 13, 131, 135, 1, 9, 135, 139, 1, 2, 139, 143, 1, 13, 143, 0, 99, 2, 0, 14, 0
]


def compute(op_code: list):
    at = 0

    while op_code[at] != 99:
        if op_code[at] == 1:
            op_code[op_code[at + 3]] = op_code[op_code[at + 1]] + op_code[op_code[at + 2]]
        elif op_code[at] == 2:
            op_code[op_code[at + 3]] = op_code[op_code[at + 1]] * op_code[op_code[at + 2]]
        at += 4

    return op_code


if __name__ == "__main__":
    # Part 1
    print("Resulted opcode: ", compute(OP_CODE.copy()))

    # Part 2, find noun and verb for 19690720
    nouns = range(100)
    verbs = range(100)

    for noun in nouns:
        for verb in verbs:
            tmp_op_code = OP_CODE.copy()
            tmp_op_code[1], tmp_op_code[2] = noun, verb
            if compute(tmp_op_code)[0] == 19690720:
                print("FOUND: noun: ", noun, "verb: ", verb, " result: ", 100 * noun + verb)
