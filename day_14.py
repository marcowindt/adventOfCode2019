import math
import sys
from math import gcd

SIMPLE = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""

SIMPLE_2 = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""

EXAMPLE = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

EXAMPLE_2 = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""

EXAMPLE_3 = """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX"""

REACTIONS = """2 MPHSH, 3 NQNX => 3 FWHL
144 ORE => 1 CXRVG
1 PGNF => 8 KHFD
3 JDVXN => 5 FSTFV
1 ZMZL, 30 PVDSG => 6 SMBH
1 CFDNS, 2 PTZNC, 10 XCKN => 9 SKVP
1 JWNR => 1 QCVHS
10 MHRML => 1 KXNWH
4 PVDSG => 3 VBZJZ
10 TLBV => 1 ZVNH
1 PVQB, 5 JDVXN => 4 WDPCN
4 NQNX, 7 KHFD, 9 SDWSL => 6 HWVM
1 SMBH => 2 PCWR
1 CXNZD, 5 SKVP, 7 LVWTF => 9 QFQJV
2 HWVM => 7 GPXP
3 CXRVG, 3 GXNL => 8 PVDSG
1 PTZNC, 2 CFDNS => 7 LCKSX
14 NQNX, 8 FWHL => 5 XCKN
12 PVDSG, 3 PVQB => 8 TLBV
8 PVQB => 8 ZKCK
1 GPXP => 5 LCGN
5 VGNR, 1 ZMZL => 9 SMGNP
2 SMGNP => 7 CXNZD
6 SMGNP, 2 HWVM, 9 PTZNC => 7 GLMVK
18 QNZVM => 7 NLCVJ
1 JDVXN, 10 GMFW, 6 VBZJZ => 9 ZMZL
1 HCFRV, 1 ZKCK, 1 SMGNP, 1 LCKSX => 7 JXZFV
13 NLCVJ, 6 ZMZL => 7 SDWSL
3 SMBH => 4 PVQB
20 QNZVM, 1 PTZNC, 7 PVQB => 7 HFLGH
2 CXNZD => 8 VLNVF
4 GMFW => 4 JDVXN
23 VGNR => 3 HSBH
1 FWHL, 32 MPHSH => 7 ZNSV
5 WDPCN, 6 ZKCK, 3 QNZVM => 4 MWHMH
1 FSTFV, 3 ZKCK, 1 LVWTF => 9 LGHD
2 SKVP, 2 MWHMH, 12 QCVHS, 6 HFLGH, 3 NRGBW, 1 ZVNH, 2 LGHD => 4 SBQKM
13 PVQB, 2 HSBH, 5 TLBV => 9 LVWTF
6 FSTFV => 2 JWNR
7 ZKCK => 9 NRGBW
8 HFLGH, 3 KXNWH, 15 VLNVF, 2 VGNR, 2 SDMS, 10 MWHMH, 7 KHFD, 1 FSTFV => 4 WTRPM
5 SKVP => 4 SDMS
100 ORE => 7 GMFW
9 GXNL => 7 MPHSH
2 GXNL, 5 GMFW => 9 NQNX
3 SDWSL, 8 LVWTF, 2 GPXP => 5 HCFRV
140 ORE => 4 GXNL
1 WDPCN, 4 NLCVJ => 1 MHRML
1 VBZJZ => 7 PGNF
1 ZNSV => 1 CFDNS
1 GLMVK, 7 SDMS => 5 GBZRN
14 WTRPM, 93 SBQKM, 37 JXZFV, 4 NRGBW, 12 QFQJV, 24 SMBH, 3 LCGN, 15 GBZRN, 16 PCWR, 11 XCKN => 1 FUEL
1 WDPCN, 5 FWHL => 8 PTZNC
1 ZNSV => 9 VGNR
5 PGNF => 5 QNZVM"""


def convert_to_dict(ins: str):
    d = dict()
    for line in ins.split("\n"):
        left_hand, right_hand = line.split('=>')
        left_hands = left_hand.split(', ')
        lefts = []
        for left_hand in left_hands:
            temp = left_hand.split(' ')
            lefts.append((temp[1], int(temp[0])))
        _, right_hand_amount, right_hand_type = right_hand.split(' ')
        right = (right_hand_type, int(right_hand_amount))
        d[right] = lefts
    return d


# def sort_reactions(rs: dict, start: tuple):
#     sorted_rs = []
#     right_hands = [start]
#
#     while right_hands:
#         right_hand = right_hands.pop()
#         if right_hand in sorted_rs:
#             sorted_rs.remove(right_hand)
#         sorted_rs.append(right_hand)
#         for left_hand in reversed(rs[right_hand]):
#             if left_hand[0] != 'ORE':
#                 right_hands.append(find_reaction_for(rs, left_hand[0]))
#
#     return list(reversed(sorted_rs))


def find_n(first: int, second: int):
    return math.ceil(first / second)


def find_reaction_for(reactions, chemical_key: str):
    for k, v in reactions.keys():
        if k == chemical_key:
            return k, v
    return None


def is_over(overs: dict, key: str):
    if key in overs.keys():
        return overs[key]
    return 0


def find_needed_ore(reactions: dict, need: dict, over: dict=None):
    ores = 0
    if over is None:
        over = {k[0]: 0 for k in reactions.keys()}

    while len(need.keys()) > 0:
        # print(over)
        new_need = {}

        for i in range(len(need.keys())):
            chemical_k, chemical_n = need.popitem()
            if chemical_k == 'ORE':
                ores += chemical_n
                continue

            if chemical_n - is_over(over, chemical_k) <= 0:
                over[chemical_k] -= chemical_n
                continue

            k, n = find_reaction_for(reactions, chemical_k)
            times_n = find_n(chemical_n - is_over(over, chemical_k), n)
            what_is_over = times_n * n - chemical_n

            if chemical_k in over.keys():
                over[chemical_k] += what_is_over
            else:
                over[chemical_k] = what_is_over

            for chem_key, chem_n in reactions[(k, n)]:
                if chem_key in new_need.keys():
                    new_need[chem_key] += times_n * chem_n
                else:
                    new_need[chem_key] = times_n * chem_n

        need = new_need

    return ores, over


def find_maximum_fuel(reactions: dict, max_ores: int=1000000000000):
    offset = 0
    add_fuel = 1
    fuel = 1
    ores = 0

    i = 0
    prev_i = 0
    while ores != max_ores:
        last_fuel = fuel
        add_fuel *= 2
        fuel = offset + add_fuel
        ores, elems = find_needed_ore(reactions, {'FUEL': fuel})
        # print(fuel, ores, elems)
        if ores > max_ores:
            # print(ores, max_ores)
            offset = last_fuel - 1
            add_fuel = 1
            if prev_i == i - 1:
                break
            prev_i = i
        i += 1

    return fuel - 1


# def is_reaction_possible(sorted_rs: list, reactions: dict, elements: dict, at):
#     print(at)
#     needed = reactions[sorted_rs[at]]
#     for k, v in needed:
#         if k not in elements.keys() or v > elements[k]:
#             if k == 'ORE':
#                 return sorted_rs.index(possible_reactions(reactions, elements)[-1])
#             return sorted_rs.index(find_reaction_for(reactions, k))
#     return at


# def possible_reactions(rs: dict, elements: dict):
#     possibles = []
#     for (k, v), elements_needed in rs.items():
#         temp_over = elements.copy()
#         possible = True
#         for element, amount in elements_needed:
#             if element in temp_over.keys() and temp_over[element] >= amount:
#                 temp_over[element] -= amount
#             else:
#                 possible = False
#                 break
#         if possible and possible not in possibles:
#             possibles.append((k, v))
#     return possibles


# def process_reaction(reaction_input: list, reaction_output: tuple, elements: dict):
#     for element, amount in reaction_input:
#         elements[element] -= amount
#
#     if reaction_output[0] in elements.keys():
#         elements[reaction_output[0]] += reaction_output[1]
#     else:
#         elements[reaction_output[0]] = reaction_output[1]
#
#     return elements


if __name__ == "__main__":
    sys.setrecursionlimit(1087655)
    HAVE_ORES = 1000000000000

    print("Answer 1:", find_needed_ore(convert_to_dict(REACTIONS), {'FUEL': 1})[0])

    print("Answer 2:", find_maximum_fuel(convert_to_dict(REACTIONS)))
