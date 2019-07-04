def angkaPrima(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

print(angkaPrima(1))
print(angkaPrima(3))
print(angkaPrima(7))
print(angkaPrima(6))
print(angkaPrima(23))