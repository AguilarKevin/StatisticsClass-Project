
#binomial distribution
def calc_binom(num_exp, rx, ri, prob, opc):

    binom = 0
    q = (1 - prob)

    if opc == 1 or opc == 2:
        i = rx
        while i <= ri:
            binom = binom + (combination(num_exp,i) * ((prob**i) * (q**(num_exp-i))))
            i = i+1
    else:
        binom = (combination(num_exp,rx) * ((prob**rx) * (q**(num_exp-rx))))
    
    return float(binom)

#mathematical expectation
def math_expec(nump_exp, prob):
    return nump_exp * prob


def combination(n, r):
    return ((factorial(n))/(factorial(r)*factorial(n - r)))

def factorial(n):
    factorial = 1
    
    if int(n) >= 1:
        for i in range (1,int(n)+1):
            factorial = factorial * i

    return factorial