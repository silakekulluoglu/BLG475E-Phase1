'''
@Authors
Student Names: Feray Lina Yence, Fitnete Guni, Sıla Keküllüoğlu
Student IDs: 150190007, 150200913, 150210084
'''

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists."""
    common_set = set(l1) & set(l2)  # Set intersection
    return sorted(list(common_set))