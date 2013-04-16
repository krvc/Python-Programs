"""

problem-7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?

"""

max_num = 10001
count = 1
number = 3


def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    
    if not isinstance(n, int):
        raise TypeError, "argument must be a positive integer"
    if n < 1:
        raise ValueError, "Argument must be a positive integer"
    
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
    
   
    
while(True):
    if isprime(number):
        count+=1
    if count >= max_num:
        break
    number+= 1
print number
