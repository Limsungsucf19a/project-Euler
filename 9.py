for a in range(1,1000):
    for b in range(1,a):
        if a**2 + b**2 == (1000 - (a + b))**2:
            c = 1000 - (a + b)
            print(a, b, c)
            print(a * b * c)
            break
