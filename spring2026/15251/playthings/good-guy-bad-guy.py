from sympy import divisors

def find_d(n, cells):
    best = 0
    for div in divisors(cells - 1):
        if div <= 2 ** n:
            best = div
        else:
            return best
    return best

def f(n):
    extra = 251 % n
    cells = 251 // n

    # For conceptual reasons
    if n == 251:
        d = 2
    else:
        d = find_d(n, cells)

    # We can equidistribute the cells to have values in 1...d
    # where d is some number such that cells mod d = 1 and d <= 2^n 

    cells_in_capture = cells // d + 1

    return cells_in_capture * n + extra

for n in range(1, 20):
    print(f"f({n}) = {f(n)}")
