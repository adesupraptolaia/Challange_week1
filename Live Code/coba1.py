#cek bilangan prima
def cekprima(n):
    if n <= 1 :
        return False
    count = 0
    for i in range(1, n+1):
        if n%i == 0:
            count +=1
    if count==2:
        return True
    else:
        return False

#fungsi untuk full prima
def fullPrima(n):
    if cekprima(n) == True:
        #cek bilangan satuannya
        while (n != 0):
            temp = n % 10
            if cekprima(temp) == True:
                n = int(n/10)
            else:
                return False
        return True
    else:
        return False

def setelahfullprima(n):
    n += 1
    while(fullPrima(n)==False):
        n+=1
    return n

print(setelahfullprima(100))

print(fullPrima(102))
# print(fullPrima(3))
# print(fullPrima(11))
# print(fullPrima(13))
# print(fullPrima(23))
# print(fullPrima(29))
# print(fullPrima(37))
# print(fullPrima(41))
# print(fullPrima(43))
# print(fullPrima(1))