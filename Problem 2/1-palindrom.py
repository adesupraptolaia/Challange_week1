def palindrom(kata):
    panjang_kata = len(kata)
    test = True
    for i in range(panjang_kata):
        if kata[i] != kata[(-(i+1))]:
            test = False
    return test

print(palindrom('katak'))
print(palindrom('blanket'))
print(palindrom('civic'))
print(palindrom('kasur rusak'))
print(palindrom('mister'))
