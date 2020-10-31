def calc_binom(num_exp, r, prob,):
    binom = 0
    q = (1 - prob)
    binom = (combination(num_exp,r) * ((prob**r) * (q**(num_exp-r))))
    return float(binom)


def combination(n, r):
    return ((factorial(n))/(factorial(r)*factorial(n - r)))

def factorial(n):
    factorial = 1
    
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i

    return factorial