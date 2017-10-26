from math import sqrt

def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    square_root = sqrt(discriminant)
    root1 = (-b- square_root) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        root2 = (-b + square_root) / (2 * a)
        return root1, root2
