import math
from decimal import Decimal, getcontext
from math import gcd
import numpy as np

ASTEROIDS = """.............#..#.#......##........#..#
.#...##....#........##.#......#......#.
..#.#.#...#...#...##.#...#.............
.....##.................#.....##..#.#.#
......##...#.##......#..#.......#......
......#.....#....#.#..#..##....#.......
...................##.#..#.....#.....#.
#.....#.##.....#...##....#####....#.#..
..#.#..........#..##.......#.#...#....#
...#.#..#...#......#..........###.#....
##..##...#.#.......##....#.#..#...##...
..........#.#....#.#.#......#.....#....
....#.........#..#..##..#.##........#..
........#......###..............#.#....
...##.#...#.#.#......#........#........
......##.#.....#.#.....#..#.....#.#....
..#....#.###..#...##.#..##............#
...##..#...#.##.#.#....#.#.....#...#..#
......#............#.##..#..#....##....
.#.#.......#..#...###...........#.#.##.
........##........#.#...#.#......##....
.#.#........#......#..........#....#...
...............#...#........##..#.#....
.#......#....#.......#..#......#.......
.....#...#.#...#...#..###......#.##....
.#...#..##................##.#.........
..###...#.......#.##.#....#....#....#.#
...#..#.......###.............##.#.....
#..##....###.......##........#..#...#.#
.#......#...#...#.##......#..#.........
#...#.....#......#..##.............#...
...###.........###.###.#.....###.#.#...
#......#......#.#..#....#..#.....##.#..
.##....#.....#...#.##..#.#..##.......#.
..#........#.......##.##....#......#...
##............#....#.#.....#...........
........###.............##...#........#
#.........#.....#..##.#.#.#..#....#....
..............##.#.#.#...........#....."""

EXAMPLE = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""

EXAMPLE_TWO = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###."""

EXAMPLE_THREE = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""

EXAMPLE_FOUR = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""


def asteroids_to_list(asteroid_map: str):
    point_list = []
    asteroid_map = asteroid_map.split('\n')
    for x in range(len(asteroid_map[0])):
        for y in range(len(asteroid_map)):
            asteroid_point = asteroid_map[y][x]
            if asteroid_point == "#":
                point_list.append((x, y))
    return point_list


def asteroid_sights_dict(asteroid_belt: list):
    asteroid_sights = dict()

    deleted = []

    for asteroid in asteroid_belt:
        asteroid_sights[asteroid] = asteroid_belt.copy()
        for other_asteroid in asteroid_belt:
            if asteroid == other_asteroid:
                if other_asteroid in asteroid_sights[asteroid]:
                    asteroid_sights[asteroid].remove(other_asteroid)
                continue
            distance_x = abs(asteroid[0] - other_asteroid[0])
            distance_y = abs(asteroid[1] - other_asteroid[1])

            point_range = gcd(distance_x, distance_y)

            if point_range > 1:
                # it is possible there are asteroids between these points
                point_x, point_y = other_asteroid[0], other_asteroid[1]
                for _ in range(point_range - 1):
                    if other_asteroid[0] > asteroid[0]:
                        point_x = point_x - distance_x / point_range
                    else:
                        point_x = point_x + distance_x / point_range

                    if other_asteroid[1] > asteroid[1]:
                        point_y = point_y - distance_y / point_range
                    else:
                        point_y = point_y + distance_y / point_range

                    if (point_x, point_y) in asteroid_belt:
                        deleted.append(other_asteroid)
                        if other_asteroid in asteroid_sights[asteroid]:
                            asteroid_sights[asteroid].remove(other_asteroid)

    return asteroid_sights


def calc_best_point(asteroid_belt: str):
    asteroid_sights = asteroid_sights_dict(asteroids_to_list(asteroid_belt))

    best_asteroid = (-1, -1), 0

    for asteroid, sights in asteroid_sights.items():
        if len(sights) > best_asteroid[1]:
            best_asteroid = asteroid, len(sights)

    return best_asteroid


def vector_angle(origin: tuple, point: tuple):
    vec1 = (0, 1)
    vec2 = (point[0] - origin[0], origin[1] - point[1])
    vec1 = np.array(vec1)   # / np.linalg.norm(np.array(vec1))
    vec2 = np.array(vec2)   # / np.linalg.norm(np.array(vec2))

    angle_prev = np.arccos(np.dot(vec1, vec2) / (np.sqrt(np.dot(vec1, vec1)) * np.sqrt(np.dot(vec2, vec2))))
    angle = 2 * math.pi - angle_prev if vec2[0] < 0 else angle_prev
    # print(origin, point, ": ", vec1, vec2, ": ", angle, angle_prev)
    return angle


def sort_clockwise(points: list, origin: tuple):
    angles = dict()

    for point in points:
        angle_key = vector_angle(origin, point)
        angles[angle_key] = point

    return [angles[angle_key] for angle_key in sorted(angles.keys())]


def vaporize(asteroid_belt: str, from_coordinate: tuple, find_index: int):
    deleted = []
    asteroid_belt = asteroids_to_list(asteroid_belt)

    while len(deleted) <= find_index:
        asteroid_sights = asteroid_sights_dict(asteroid_belt)
        clockwised = sort_clockwise(asteroid_sights[from_coordinate], from_coordinate)
        deleted.extend(clockwised)
        for asteroid in asteroid_sights[from_coordinate]:
            asteroid_belt.remove(asteroid)

    return deleted, deleted[find_index]


if __name__ == "__main__":
    # Part 1
    asteroid_point, sight_size = calc_best_point(ASTEROIDS)
    print("Answer 1:", asteroid_point, sight_size, "asteroids")

    # Part 2
    vaporized, found_vaporized = vaporize(ASTEROIDS, asteroid_point, len(asteroids_to_list(ASTEROIDS)) - 2)
    print("Answer 2:", vaporized[199], "=", vaporized[199][0] * 100 + vaporized[199][1])
