def factors(n):
    factors_list = []
    for i in range(1,n+1):
        if n%i == 0:
            factors_list.append(i)
    return factors_list

def HCF(m,k):
    factors_of_m = factors(m)
    factors_of_k = factors(k)

    hcf = 1

    for i in factors_of_m:
        for j in factors_of_k:
            if i==j:
                hcf = i
    return hcf

a, b = 12, 18
print("HCF of",a,"and",b,"is",HCF(a,b))
