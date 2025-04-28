def bf(planet1, planet2):
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", 
"Neptune"]
    planet_indices = {planet: i for i, planet in enumerate(planets)}

    if planet1 not in planet_indices or planet2 not in planet_indices:
        return tuple()

    planet1_index, planet2_index = planet_indices[planet1], planet_indices[planet2]
    return sorted(planets[(planet1_index + 1):(planet2_index - 1)])