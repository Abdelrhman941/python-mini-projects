def gen_primes(N):
    primes = set()
    for n in range(2, N):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n

print(*gen_primes(100))
#####################################
def pn(n):
    pnn =[]
    for h in range(2,n+1):
        divisible = True
        for j in range(h-1,1,-1):
            if (h%j) == 0:
                divisible = False
        if divisible :
            pnn. append(h)

    print (pnn)
    return pnn

pn(100)