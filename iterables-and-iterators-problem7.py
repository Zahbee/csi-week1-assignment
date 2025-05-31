import math

def combinations(n, k):
   
    if k < 0 or k > n:
        return 0
    
    # C(n, k) = n! / (k! * (n-k)!)
    numerator = math.factorial(n)
    denominator = math.factorial(k) * math.factorial(n - k)
    
    return numerator // denominator  # Use integer division as combinations are always integers

def solve():
    N = int(input())
    chars = input().split()
    K = int(input())

    count_a = 0
    for char in chars:
        if char == 'a':
            count_a += 1

    # Total number of ways to choose K indices from N
    total_combinations = combinations(N, K)

    # Number of ways to choose K indices such that none of them are 'a'
    # This means choosing K indices only from the characters that are not 'a'
    non_a_count = N - count_a
    
    combinations_without_a = combinations(non_a_count, K)

    # If K is greater than the number of non-'a' characters, it's impossible
    # to choose K indices without 'a', so combinations_without_a will be 0.
    # The combinations function handles this (returns 0 if k > n).

    if total_combinations == 0:
        # This condition should ideally not be met given 1 <= K <= N.
        # But for robustness, if for some reason total_combinations is 0,
        # it implies no valid selections, so probability of at least one 'a' is 0.
        print(f"{0.0:.4f}")
        return

    # Probability of selecting K indices with no 'a'
    prob_without_a = combinations_without_a / total_combinations

    # Probability of selecting at least one 'a'
    prob_at_least_one_a = 1 - prob_without_a

    print(f"{prob_at_least_one_a:.4f}")

solve()
