"""
problem-2:

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

"""

result = 0

def fibo(n):
    """Fibanocci sequence"""
    a, b = 0, 1
    li = []

    while b < n:
        a, b = b, a + b
        li.append(b)

    return li

fib_list = fibo(4000000)

for i in fib_list:
    if i % 2 == 0:
        result = result + i

print result 
