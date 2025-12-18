#!/usr/bin/env python
import matplotlib.pyplot as plt
import argparse

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

    dp = [[0 for _ in range(x+1)] for _ in range(x+1)]

    # Base Case
    dp[0][0] = 1

    # Bottom-up table filling
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i-1][j-1] + j * dp[i-1][j]

    return dp[x]

def probability_distribution(m: int, n: int) -> dict:
    """
    Computes the probability distribution of the number of unique
    heroes obtained after m summons of heroes with n heroes in the
    game. 

    Assumes:
        - Hero summons are independent of all previous summons and 
        give equal probability of obtaining any hero in the game,
        regardless of which ones are currently unlocked.
    
    Returns: 
        - A dictionary d, where d[k] gives the probability of obtaining k 
        unique heroes for all 1 <= k <= m. 
    """
    stirling_numbers = stirling(m)
    denom = n ** m

    # The maximum number of unique heroes that can be obtained
    upper_bound = min(m, n)
    dist = {}

    for k in range(1, upper_bound+1):
        numer = stirling_numbers[k] * falling_factorial(n, k)
        dist[k] = numer / denom
    
    # Quick sanity check to verify probabilities add to 1
    assert(abs(sum(dist.values()) - 1) < 10 ** -3)
    return dist

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Finds the probability distribution of unique heroes from repeated hero summons.'
    )
    
    print(probability_distribution(30, 20))