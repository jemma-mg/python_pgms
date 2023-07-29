def factors(n):
    factors_list = []
    for i in range(1, n+1):
        if n%i == 0:
            factors_list.append(i)
    return (factors_list)

## prime numbers have only 2 fators 1 and itself
def prime(n):
    return(factors(n) == [1,n])

def check_prime(n):
    return(len(factors(n))==2)

print(prime(2))
print(check_prime(3))

print(prime(9))
print(check_prime(18))

## prime numbers from 1-100
prime_list = []
for i in range(1,101):
    if prime(i):
        prime_list.append(i)
print(prime_list)
