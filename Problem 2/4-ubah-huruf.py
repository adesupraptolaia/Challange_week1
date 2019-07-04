huruf = ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

huruf1 = "abcdefghijklmnopqrstuvwxyzaABCDEFGHIJKLMNOPQRSTUVWXYZA"

def ubahHuruf(kata):
    kata1=""
    for i in range(len(kata)):
        index = 0
        for k in range(len(huruf1)):
            if kata[i] == huruf1[k]:
                index += (k+1)
                break
        kata1 += huruf1[index]
    return kata1

print(ubahHuruf('wow'))
print(ubahHuruf('developer'))
print(ubahHuruf('keren'))
print(ubahHuruf('semangat'))