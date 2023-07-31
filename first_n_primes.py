def factors(n):
    factors_list = []
    for i in range(1, n+1):
        if n%i == 0:
            factors_list.append(i)
    return (factors_list)

def prime(n):
    return(factors(n) == [1,n])

def firstprimes(n):
    count, i, primes = 0, 1,[]
    while (count < n):
        if prime(i):
            count, primes = count+1, primes+[i]
        i = i + 1
    return (primes)