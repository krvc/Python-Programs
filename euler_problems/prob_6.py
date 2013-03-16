"""
Problem-6:

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.

"""

sum_sqrs = 0
sqr_temp = 0

for i in range(1,101):
    sum_sqrs = sum_sqrs+(i*i)
    sqr_temp = sqr_temp+i
sqr_sum = sqr_temp **2
diff = sqr_sum - sum_sqrs

print diff
