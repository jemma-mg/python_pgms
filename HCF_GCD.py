def HCF(m,n):
    for i in range(1,min(m,n)+1):
        if (m % i)==0 and (n % i)==0:
            hcf = i
    return hcf

print(HCF(12,15))