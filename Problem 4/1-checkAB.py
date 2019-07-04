def checkAB(str):
    len_str = len(str)
    #list tempat indeks a dan b pada str
    index_a = []
    index_b = []
    for i in range(len_str):
        if 'a' == str[i]:
            index_a.append(i)
        if 'b' == str[i]:
            index_b.append(i)
    
    hasil = False
    #kasus kalau gak ada a atau b di str
    if index_a == [] or index_b == []:
        hasil = False
    else:
        for i in index_a:
            for k in index_b:
                if abs(i-k)==4:
                    hasil = True
                    break
    return hasil

print(checkAB('lane borrowed'))
print(checkAB('i am sick'))
print(checkAB('you are boring'))
print(checkAB('barbarian'))
print(checkAB('bacon and meat'))