#fungsi cari bilangan prima setelah n
def caribilprimasetelah(n):
    count = 0
    #count untuk hitung banyak faktor, kalo faktornya = 2 berarti prima
    while (count != 2):
        n += 1
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
    return n

def primaSegiEmpat(p, l, n):
    #buat list tempat bil prima dan ukuran listnya
    luas = p*l
    arrprima = []
    #loop untuk memasukkan bilangan prima setelah n ke array
    for i in range(luas):
        n = caribilprimasetelah(n)
        arrprima.append(n)
    
    #mencari total bilangan prima
    total = 0
    for i in range(luas):
        total += arrprima[i]
    


    print("'''")
    #print bilangan prima
    index = 0
    for i in range(l):
        tampung = ''
        for k in range(p):
            tampung += str(arrprima[index])
            if arrprima[index] < 7:
                tampung += "  "
            else:
                tampung += " "
            index += 1
        print(tampung)
    print("Total: "+str(total))
    print("'''")

primaSegiEmpat(2,3,13)
primaSegiEmpat(5,2,1)

        
    