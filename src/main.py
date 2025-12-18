import matplotlib.pyplot as plt

def falling_factorial(x: int, y: int) -> int:
    """
    Computes P(x, y) = x(x-1)...(x-y+1), a falling factorial.
    Assumes x and y are positive integers with y <= x.
    """
    res = 1
    for i in range(y):
        res *= (x - i)
    
    return res

def stirling(x: int) -> list:
    """
    This function calculates the number of ways to partition the
    set [x] = {1, 2, ..., x} into y non-empty groups, where x and y
    are positive integers.  We use bottom-up dynamic programming to do so. See the PDF
    for a derivation of this recursion + its relevance to broader hero problem.

    DP is perhaps a smidge more efficient than using the direct formula
    since we compute a whole batch of stirling numbers at once.

    Returns:
        - a list of integers l, where l[y] = S(x, y) for all 0 <= y <= x.
    """
    assert(x > 0)
    return []

