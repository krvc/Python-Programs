"""
problem-2:

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

"""


result = 0

class NoElementsBelowGivenParameter(Exception): pass
def fibo(n):
    """Fibanocci sequence"""
    a, b = 0, 1
    li = []
    
    if not isinstance(n, int):
        raise TypeError, "Parameter is not an integer."
        
        
    if not n > 1: # Number requested is too low to return non-empty sequence
        raise NoElementsBelowGivenParameter

    while b < n:
        a, b = b, a + b
        li.append(b)

    return li

fib_list = fibo(4000000)

for i in fib_list:
    if i % 2 == 0:
        result = result + i

print result 
