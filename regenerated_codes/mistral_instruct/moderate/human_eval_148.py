'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

planets = {
    "Mercury": 0,
    "Venus": 1,
    "Earth": 2,
    "Mars": 3,
    "Jupiter": 4,
    "Saturn": 5,
    "Uranus": 6,
    "Neptune": 7
}

def bf(planet1, planet2):
    if planet1 not in planets or planet2 not in planets:
        return tuple()

    index1 = planets[planet1]
    index2 = planets[planet2]

    if index1 > index2:
        index1, index2 = index2, index1

    result = []
    for planet_index in range(index1 + 1, index2):
        result.append(list(planets.keys())[planet_index])

    return tuple(result) if result else tuple()