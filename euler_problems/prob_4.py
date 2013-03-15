palan = 0

for a in range(100, 1000) :
    for b in range(100, a) :
        c = a * b
        if c > palan :
            s = str(a * b)
            if s == s[::-1] :
                palan = a * b
print palan
