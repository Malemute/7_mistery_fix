from math import sqrt

def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    sqroot = 0
    if discriminant < 0:
        return None, None
    sqroot = sqrt(discriminant)
    root1 = (-b- sqroot) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        root2 = (-b + sqroot) / (2 * a)
        return root1, root2
