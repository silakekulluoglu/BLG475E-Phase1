def triangle_area(a, h):
    if a <= 0 or h <= 0:
        raise ValueError("Base and height must be positive.")
    return 0.5 * a * h