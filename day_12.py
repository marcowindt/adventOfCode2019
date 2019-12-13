from functools import reduce
from math import gcd

EXAMPLE = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]

EXAMPLE_TWO = [[-8, -10, 0],
               [5, 5, 10],
               [2, -7, 3],
               [9, -8, -3]]

BODIES = [[7, 10, 17],
          [-2, 7, 0],
          [12, 5, 12],
          [5, -8, 6]]


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)


def get_lcm_for(your_list):
    return reduce(lambda x, y: lcm(x, y), your_list)


def velocity(first, second):
    vel = [0, 0, 0]
    vel2 = [0, 0, 0]
    for i in range(3):
        if first[i] < second[i]:
            vel[i] = 1
            vel2[i] = -1
        elif first[i] > second[i]:
            vel[i] = -1
            vel2[i] = 1
        else:
            vel[i] = 0
            vel2[i] = 0

    return vel, vel2


def brent(f, x0):
    # https://rosettacode.org/wiki/Cycle_detection#Python
    # main phase: search successive powers of two
    power = lam = 1
    tortoise = x0
    hare = f(x0)  # f(x0) is the element/node next to x0.
    while tortoise[1] != hare[1]:
        if power == lam:  # time to start a new power of two?
            tortoise = hare
            power *= 2
            lam = 0
        hare = f(hare)
        lam += 1

    # Find the position of the first repetition of length λ
    tortoise = hare = x0
    for i in range(lam):
        # range(lam) produces a list with the values 0, 1, ... , lam-1
        hare = f(hare)
    # The distance between the hare and tortoise is now λ.

    # Next, the hare and tortoise move at same speed until they agree
    mu = 0
    while tortoise[1] != hare[1]:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    return lam, mu


def update(bds, steps: int, calc_periods=True):
    cnt = 0
    found = False

    pxs = [[bds[0][0], bds[1][0], bds[2][0], bds[3][0]]]
    pys = [[bds[0][1], bds[1][1], bds[2][1], bds[3][1]]]
    pzs = [[bds[0][2], bds[1][2], bds[2][2], bds[3][2]]]

    vxs = [[0, 0, 0, 0]]
    vys = [[0, 0, 0, 0]]
    vzs = [[0, 0, 0, 0]]

    while cnt < steps and not found:
        vx = vxs[-1].copy()
        vy = vys[-1].copy()
        vz = vzs[-1].copy()

        px = pxs[-1].copy()
        py = pys[-1].copy()
        pz = pzs[-1].copy()

        add_vel_1, add_vel_2 = velocity(bds[0], bds[1])
        vx[0] += add_vel_1[0]
        vy[0] += add_vel_1[1]
        vz[0] += add_vel_1[2]

        vx[1] += add_vel_2[0]
        vy[1] += add_vel_2[1]
        vz[1] += add_vel_2[2]

        add_vel_1, add_vel_2 = velocity(bds[0], bds[2])
        vx[0] += add_vel_1[0]
        vy[0] += add_vel_1[1]
        vz[0] += add_vel_1[2]

        vx[2] += add_vel_2[0]
        vy[2] += add_vel_2[1]
        vz[2] += add_vel_2[2]

        add_vel_1, add_vel_2 = velocity(bds[0], bds[3])
        vx[0] += add_vel_1[0]
        vy[0] += add_vel_1[1]
        vz[0] += add_vel_1[2]

        vx[3] += add_vel_2[0]
        vy[3] += add_vel_2[1]
        vz[3] += add_vel_2[2]

        add_vel_1, add_vel_2 = velocity(bds[1], bds[2])
        vx[1] += add_vel_1[0]
        vy[1] += add_vel_1[1]
        vz[1] += add_vel_1[2]

        vx[2] += add_vel_2[0]
        vy[2] += add_vel_2[1]
        vz[2] += add_vel_2[2]

        add_vel_1, add_vel_2 = velocity(bds[1], bds[3])
        vx[1] += add_vel_1[0]
        vy[1] += add_vel_1[1]
        vz[1] += add_vel_1[2]

        vx[3] += add_vel_2[0]
        vy[3] += add_vel_2[1]
        vz[3] += add_vel_2[2]

        add_vel_1, add_vel_2 = velocity(bds[2], bds[3])
        vx[2] += add_vel_1[0]
        vy[2] += add_vel_1[1]
        vz[2] += add_vel_1[2]

        vx[3] += add_vel_2[0]
        vy[3] += add_vel_2[1]
        vz[3] += add_vel_2[2]

        for i in range(4):
            bds[i][0] += vx[i]
            bds[i][1] += vy[i]
            bds[i][2] += vz[i]

            px[i] += vx[i]
            py[i] += vy[i]
            pz[i] += vz[i]

        vxs.append(vx)
        vys.append(vy)
        vzs.append(vz)

        pxs.append(px)
        pys.append(py)
        pzs.append(pz)

        cnt += 1

    if calc_periods:
        periods_ = [find_period([p for p in zip(pxs[1:], pxs[2:], pxs[:-1])]),
                    find_period([p for p in zip(pys[1:], pys[2:], pys[:-1])]),
                    find_period([p for p in zip(pzs[1:], pzs[2:], pzs[:-1])]),
                    find_period([v for v in zip(vxs[1:], vxs[2:], vxs[:-1])]),
                    find_period([v for v in zip(vys[1:], vys[2:], vys[:-1])]),
                    find_period([v for v in zip(vzs[1:], vzs[2:], vzs[:-1])])]

        periods_1 = [p[0] for p in periods_ if p is not None]
        return bds, cnt, periods_, get_lcm_for(periods_1), energy(pxs[-1], pys[-1], pzs[-1], vxs[-1], vys[-1], vzs[-1])

    return bds, cnt, [], 0, energy(pxs[-1], pys[-1], pzs[-1], vxs[-1], vys[-1], vzs[-1])


def find_period(ls: list, x_i=5):
    def next_elem(x: tuple):
        return x[0] + 1, ls[x[0] + 1]

    halt = False
    while not halt:
        try:
            brent_me = brent(next_elem, (x_i, ls[x_i]))
            return brent_me
        except IndexError:
            x_i += 1
            print("x_i =", x_i)
            halt = x_i > 20


def energy(xs: list, ys: list, zs: list, vx: list, vy: list, vz: list):
    total = 0
    for i in range(4):
        pos = abs(xs[i]) + abs(ys[i]) + abs(zs[i])
        vel = abs(vx[i]) + abs(vy[i]) + abs(vz[i])
        total += pos * vel
    return total


if __name__ == "__main__":
    # Part 1                          must copy, since python does not copy inner lists automatically
    _, step, b_periods, b_lcm, e_1 = update([b.copy() for b in BODIES], 1000, calc_periods=False)
    print("Answer 1: Energy:", e_1, "Steps:", step, "Period:", b_lcm, "Periods:", b_periods)

    # Part 2
    _, step, d_periods, d_lcm, e_2 = update(BODIES.copy(), 500000)
    print("Answer 2: Energy:", e_2, "Steps:", step, "Period:", d_lcm, "Periods:", d_periods)
