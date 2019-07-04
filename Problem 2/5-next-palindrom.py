def cek_polindrom(n):
    sisa = 0
    balik = 0
    asli = n
    while (n !=0 ):
        sisa = n % 10
        balik = balik*10 + sisa
        n = int(n/10)
    if balik == asli :
        return 1
    else:
        return 0

def angkapalindrome(k):
    k += 1
    while(cek_polindrom(k)== 0):
        k +=1
    return k


print(angkapalindrome(8))
print(angkapalindrome(10))
print(angkapalindrome(117))
print(angkapalindrome(175))
print(angkapalindrome(1000))