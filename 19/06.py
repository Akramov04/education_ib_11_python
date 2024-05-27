def find_farthest_orbit(list_of_orbits):
    res = []
    for i in list_of_orbits:
        a, b = i
        if a == b:
            a, b = 0, 0
        res.append(3.1459 * a * b)
    return list_of_orbits[res.index(max(res))]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))