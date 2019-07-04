def pasanganTerbesar(angka):
    strangka = str(angka)
    max = angka % 100
    for i in range(len(strangka)-1):
        test = 10*int(strangka[i]) + int(strangka[i+1])
        if max < test:
            max = test
    return max


print(pasanganTerbesar(641573))
print(pasanganTerbesar(12783456))
print(pasanganTerbesar(910233))
print(pasanganTerbesar(71856421))
print(pasanganTerbesar(79918293))
