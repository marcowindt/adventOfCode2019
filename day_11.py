import numpy as np

SIZE = 100
OP_CODE = [3, 8, 1005, 8, 325, 1106, 0, 11, 0, 0, 0, 104, 1, 104, 0, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 108,
           0, 8, 10, 4, 10, 101, 0, 8, 28, 2, 3, 7, 10, 2, 1109, 3, 10, 2, 102, 0, 10, 2, 1005, 12, 10, 3, 8, 102, -1,
           8, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 101, 0, 8, 67, 2, 109, 12, 10, 1, 1003, 15, 10, 3, 8,
           1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 108, 1, 8, 10, 4, 10, 101, 0, 8, 96, 3, 8, 102, -1, 8, 10, 101, 1,
           10, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 1002, 8, 1, 119, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 1008, 8,
           0, 10, 4, 10, 101, 0, 8, 141, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1001, 8, 0,
           162, 1, 106, 17, 10, 1006, 0, 52, 1006, 0, 73, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 108, 1, 8, 10,
           4, 10, 1001, 8, 0, 194, 1006, 0, 97, 1, 1004, 6, 10, 1006, 0, 32, 2, 8, 20, 10, 3, 8, 102, -1, 8, 10, 101, 1,
           10, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 102, 1, 8, 231, 1, 1, 15, 10, 1006, 0, 21, 1, 6, 17, 10, 2, 1005, 8,
           10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 1, 8, 10, 4, 10, 102, 1, 8, 267, 2, 1007, 10, 10, 3, 8,
           1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 102, 1, 8, 294, 1006, 0, 74, 2, 1003, 2, 10,
           1, 107, 1, 10, 101, 1, 9, 9, 1007, 9, 1042, 10, 1005, 10, 15, 99, 109, 647, 104, 0, 104, 1, 21101,
           936333018008, 0, 1, 21101, 342, 0, 0, 1106, 0, 446, 21102, 937121129228, 1, 1, 21101, 0, 353, 0, 1105, 1,
           446, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 1, 3, 10, 104,
           0, 104, 0, 3, 10, 104, 0, 104, 1, 21101, 0, 209383001255, 1, 21102, 400, 1, 0, 1106, 0, 446, 21101, 0,
           28994371675, 1, 21101, 411, 0, 0, 1105, 1, 446, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 0, 21101,
           867961824000, 0, 1, 21101, 0, 434, 0, 1106, 0, 446, 21102, 1, 983925674344, 1, 21101, 0, 445, 0, 1106, 0,
           446, 99, 109, 2, 21201, -1, 0, 1, 21102, 40, 1, 2, 21101, 477, 0, 3, 21102, 467, 1, 0, 1106, 0, 510, 109, -2,
           2106, 0, 0, 0, 1, 0, 0, 1, 109, 2, 3, 10, 204, -1, 1001, 472, 473, 488, 4, 0, 1001, 472, 1, 472, 108, 4, 472,
           10, 1006, 10, 504, 1101, 0, 0, 472, 109, -2, 2106, 0, 0, 0, 109, 4, 1201, -1, 0, 509, 1207, -3, 0, 10, 1006,
           10, 527, 21102, 1, 0, -3, 21202, -3, 1, 1, 21201, -2, 0, 2, 21102, 1, 1, 3, 21102, 1, 546, 0, 1106, 0, 551,
           109, -4, 2105, 1, 0, 109, 5, 1207, -3, 1, 10, 1006, 10, 574, 2207, -4, -2, 10, 1006, 10, 574, 22101, 0, -4,
           -4, 1105, 1, 642, 21202, -4, 1, 1, 21201, -3, -1, 2, 21202, -2, 2, 3, 21101, 0, 593, 0, 1105, 1, 551, 22102,
           1, 1, -4, 21101, 1, 0, -1, 2207, -4, -2, 10, 1006, 10, 612, 21102, 1, 0, -1, 22202, -2, -1, -2, 2107, 0, -3,
           10, 1006, 10, 634, 21201, -1, 0, 1, 21101, 634, 0, 0, 105, 1, 509, 21202, -2, -1, -2, 22201, -4, -2, -4, 109,
           -5, 2106, 0, 0]


def print_canvas(canvas: list, only_white=True):
    p_can = []
    for i in range(SIZE):
        p_can.append([])
        for _ in range(SIZE):
            p_can[i].append('.')

    for i, ii in zip(range(SIZE), range(SIZE - 1, -1, -1)):
        for j, jj in zip(range(SIZE), range(SIZE - 1, -1, -1)):
            if only_white:
                p_can[i][j] = ' ' if canvas[ii][j] == '.' else '█'
            else:
                p_can[i][j] = canvas[ii][j]

    canvas = np.array(p_can.copy())

    for canvas_line in canvas:
        if not only_white:
            print(''.join(canvas_line))
        else:
            if '█' in canvas_line:
                print(''.join(canvas_line))


def rotation_matrix(theta):
    c, s = np.cos(theta), np.sin(theta)
    return np.array(((c, -s), (s, c)))


def paint_bot(op_code: list, canvas: list, position: tuple):
    at = 0
    relative = 0
    did_paint = False

    visited = [position]

    rotate_left = rotation_matrix(np.pi / 2)
    rotate_right = rotation_matrix(-np.pi / 2)

    cur_position = position, (0, 1)  # 0, 1 = up, 1, 0 = right, 0, -1 = down, -1, 0 = left

    while op_code[at] != 99:
        operator = str(op_code[at])
        operator = [int(x) for x in operator.zfill(5)]

        if operator[-1] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if operator[2] == 0:
                first_value = op_code[at + 1]
            elif operator[2] == 2:
                first_value = relative + op_code[at + 1]
            else:
                first_value = at + 1

            if operator[1] == 0:
                second_value = op_code[at + 2]
            elif operator[1] == 2:
                second_value = relative + op_code[at + 2]
            else:
                second_value = at + 2

            if operator[0] == 0:
                third_value = op_code[at + 3]
            elif operator[0] == 2:
                third_value = relative + op_code[at + 3]
            else:
                third_value = at + 3
        else:
            first_value, second_value, third_value = 0, 0, 0

        if operator[-1] == 1:
            op_code[third_value] = op_code[first_value] + op_code[second_value]
            at += 4
        elif operator[-1] == 2:
            op_code[third_value] = op_code[first_value] * op_code[second_value]
            at += 4
        elif operator[-1] == 3:
            # input
            op_code[first_value] = 0 if canvas[cur_position[0][1]][cur_position[0][0]] == '.' else 1
            at += 2
        elif operator[-1] == 4:
            # output
            out = op_code[first_value]
            if not did_paint:
                if out == 0:
                    canvas[cur_position[0][1]][cur_position[0][0]] = '.'    # if out == 0 else '#'
                else:
                    canvas[cur_position[0][1]][cur_position[0][0]] = '█'
                did_paint = True
                # print_canvas(canvas, cur_position)
            else:
                if out == 0:
                    # turn left
                    rotated = np.dot(rotate_left, np.array(cur_position[1]))
                    rotated = int(rotated[0]), int(rotated[1])
                else:
                    # turn right
                    rotated = np.dot(rotate_right, np.array(cur_position[1]))
                    rotated = int(rotated[0]), int(rotated[1])

                new_pos = cur_position[0][0] + rotated[0], cur_position[0][1] + rotated[1]
                # print(out, cur_position, (new_pos, rotated))
                cur_position = new_pos, rotated

                visited.append(cur_position[0])

                did_paint = False
            at += 2
        elif operator[-1] == 5:
            # jump if true
            if op_code[first_value] != 0:
                at = op_code[second_value]
            else:
                at += 3
        elif operator[-1] == 6:
            # jump if false
            if op_code[first_value] == 0:
                at = op_code[second_value]
            else:
                at += 3
        elif operator[-1] == 7:
            # less than
            if op_code[first_value] < op_code[second_value]:
                op_code[third_value] = 1
            else:
                op_code[third_value] = 0
            at += 4
        elif operator[-1] == 8:
            # equals
            if op_code[first_value] == op_code[second_value]:
                op_code[third_value] = 1
            else:
                op_code[third_value] = 0
            at += 4
        elif operator[-1] == 9:
            # increase / decrease relative address
            relative += op_code[first_value]
            at += 2

    return op_code, visited, canvas, cur_position


if __name__ == "__main__":
    init_canvas = []
    for i in range(SIZE):
        init_canvas.append([])
        for _ in range(SIZE):
            init_canvas[i].append('.')

    ops, vis, can, pos = paint_bot(OP_CODE + [0] * 500, init_canvas, (int(SIZE / 2 - 1), int(SIZE / 2 - 1)))

    print("Answer 1:", len(set(vis)))

    init_canvas = []
    for i in range(SIZE):
        init_canvas.append([])
        for _ in range(SIZE):
            init_canvas[i].append('.')

    init_canvas[int(SIZE / 2 - 1)][int(SIZE / 2 - 1)] = '█'

    ops, vis, can, pos = paint_bot(OP_CODE + [0] * 500, init_canvas, (int(SIZE / 2 - 1), int(SIZE / 2 - 1)))
    print("Answer 2:")
    print_canvas(can)
