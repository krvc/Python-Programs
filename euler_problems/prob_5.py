"""

Problem-5:

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from
1 to 20?

"""

def greatcommondiv(x, y):
    if(y == 0):
        return x
    return greatcommondiv(y, x % y)


def leastcomnfact(x, y):
    
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError, "Parameters must be integers"
    
    if x < 1:
        raise ValueError, "parameters must be positive"
    
    return y * x / greatcommondiv(x, y)

ans = 2

for i in range(3, 20):
    ans = leastcomnfact(ans, i)

print ans
