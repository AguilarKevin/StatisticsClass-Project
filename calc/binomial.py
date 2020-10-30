def calc_binom(ni, pi, x, xi):
    binom = 0
    intervalos = x + xi
    i = x
    while i < xi:
        temp = 0
        xx = i
        n = ni
        q = (1 - pi)
        temp = ((combination(n, xx))* (pi**xx)) * (q**(ni - xx))
        binom += temp

    return binom


def combination(n, r):
    com = 0
    nr = (n - r)

    com = ((factorial(n))/(factorial(r)*factorial(nr)))
    return com



def factorial(n):
    factorial = 1
    
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i

    return factorial

print(factorial(6))