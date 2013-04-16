"""
Problem:3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def prim_fact(n):
    "Returns all the prime factors of a positive integer"
    
    if n < 1:
        raise ValueError, "Parameter must be at least 1."
    
    factors = []
    d = 2
    while (n > 1):
        while (n%d==0):
            factors.append(d)
            n = n / d
        d = d + 1

    return factors


pf = prim_fact(600851475143) 
largest_prime_factor = pf[-1]
print largest_prime_factor
