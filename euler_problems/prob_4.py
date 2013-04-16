"""

Problem:

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""


palan = 0

for a in range(100, 1000) :
    for b in range(100, a) :
        c = a * b
        if c > palan :
            s = str(a * b)
            if s == s[::-1] :
                palan = a * b
print palan
