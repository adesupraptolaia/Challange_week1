def digitPerkalianMinimum(angka):
    #array tempat pasangan faktor
    arr_faktor = []

    #looping untuk mencari faktor
    for i in range(1,angka+1):
        temp ='' #tempat sementara 
        if angka % i == 0 :
            temp += str(i)
            temp += str(int(angka/i))
            arr_faktor.append(temp)
    
    hasil = len(arr_faktor[0]) #hasil akhir
    #membandingkan hasil akhir terkecil
    for i in range(len(arr_faktor)):
        if hasil > len(arr_faktor[i]):
            hasil = len(arr_faktor[i])
    
    return hasil

print(digitPerkalianMinimum(24))
print(digitPerkalianMinimum(90))
print(digitPerkalianMinimum(20))
print(digitPerkalianMinimum(179))
print(digitPerkalianMinimum(1))
