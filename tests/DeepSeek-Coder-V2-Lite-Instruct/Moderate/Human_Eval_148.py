def check(candidate):
    assert candidate("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert candidate("Earth", "Mercury") == ("Venus",)
    assert candidate("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert candidate("Neptune", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus")
    assert candidate("Earth", "Earth") == ()