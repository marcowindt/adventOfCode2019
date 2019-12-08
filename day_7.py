from itertools import product, permutations

OP_CODE = [
    3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 38, 63, 80, 105, 118, 199, 280, 361, 442, 99999, 3, 9, 102, 5, 9, 9, 1001,
    9, 3, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 1001, 9, 4, 9, 102, 4, 9, 9, 101, 4, 9, 9, 102, 2, 9, 9, 101, 2, 9, 9, 4, 9,
    99, 3, 9, 1001, 9, 5, 9, 102, 4, 9, 9, 1001, 9, 4, 9, 4, 9, 99, 3, 9, 101, 3, 9, 9, 1002, 9, 5, 9, 101, 3, 9, 9,
    102, 5, 9, 9, 101, 3, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 1001, 9, 4, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9,
    1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9,
    2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4,
    9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3,
    9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002,
    9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9,
    4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3,
    9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9,
    102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9,
    9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9,
    99, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9,
    1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9,
    1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 99
]

EXAMPLE = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
EXAMPLE_TWO = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23,
               101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
EXAMPLE_THREE = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
                 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]
EXAMPLE_P2 = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
              27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
EXAMPLE_P2_TWO = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
                  -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
                  53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]


def compute(op_code: tuple, phase_setting: int, input_value: int, phase_input=False):
    at = op_code[1]
    op_code = op_code[0]

    while op_code[at] != 99:
        operator = str(op_code[at])
        operator = [int(x) for x in operator.zfill(5)]

        # print(operator)
        # print(op_code)

        if operator[-1] in [1, 2, 5, 6, 7, 8]:
            if operator[2] == 0:
                first_value = op_code[op_code[at + 1]]
            else:
                first_value = op_code[at + 1]

            if operator[1] == 0:
                second_value = op_code[op_code[at + 2]]
            else:
                second_value = op_code[at + 2]
        else:
            first_value, second_value = 0, 0

        if operator[-1] == 1:
            op_code[op_code[at + 3]] = first_value + second_value
            at += 4
        elif operator[-1] == 2:
            op_code[op_code[at + 3]] = first_value * second_value
            at += 4
        elif operator[-1] == 3:
            # input
            # ins = input("Please specify your input and press enter: ")
            if not phase_input:
                ins = phase_setting
                phase_input = True
            else:
                ins = input_value
            op_code[op_code[at + 1]] = ins
            at += 2
        elif operator[-1] == 4:
            # output
            if operator[2] == 1:
                # print(op_code[at + 1])
                return (op_code, at + 2), op_code[at + 1]
            else:
                # print(op_code[op_code[at + 1]])
                return (op_code, at + 2), op_code[op_code[at + 1]]
            # at += 2
        elif operator[-1] == 5:
            # jump if true
            if first_value != 0:
                at = second_value
            else:
                at += 3
        elif operator[-1] == 6:
            # jump if false
            if first_value == 0:
                at = second_value
            else:
                at += 3
        elif operator[-1] == 7:
            if operator[0] == 0:
                third_value = op_code[at + 3]
            else:
                third_value = at + 3
            # less than
            if first_value < second_value:
                op_code[third_value] = 1
            else:
                op_code[third_value] = 0
            at += 4
        elif operator[-1] == 8:
            if operator[0] == 0:
                third_value = op_code[at + 3]
            else:
                third_value = at + 3
            # equals
            if first_value == second_value:
                op_code[third_value] = 1
            else:
                op_code[third_value] = 0
            at += 4

    return (op_code, at), -1


if __name__ == "__main__":
    # Part 1
    output = []
    for phase in permutations(range(5)):
        input_value = 0
        for x in phase:
            program, input_value = compute((OP_CODE.copy(), 0), x, input_value)

        output.append(input_value)

    print("Answer 1:", max(output))

    # Part 2
    output = []
    for phase in permutations(range(5, 10)):
        input_value = 0
        programs = [(OP_CODE.copy(), 0) for _ in range(5)]

        phase_inserted = False
        while input_value != -1:
            for x, i in zip(phase, range(5)):
                programs[i], input_value = compute(programs[i], x, input_value, phase_input=phase_inserted)

            phase_inserted = True

            output.append(input_value)

    print("Answer 2:", max(output))
