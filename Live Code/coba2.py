alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

#print(alfabet[3])
# cek kesamaan dua array
x = [1,2,3]
y = [1,2,4]
#print(x==y)
#x[1] += 7
# x[1][1] += 7
#x[2] += 7
#print(x)
#print(x==y)

x = [[0,1], [0,2], [0,3]]
y = [[0,4], [0,5], [0,6]]
#print(x == y)

indeks = [0 for i in range(len(alfabet))]
#print(indeks)
#fungsi sorting huruf dengan output arr
def string_acak(kata1, kata2):
    indeks_kata1 = [0 for i in range(len(alfabet))]
    indeks_kata2 = [0 for i in range(len(alfabet))]
    #memasukkan indeks dari kata1 ke indeks_kata1

    for i in range(len(kata1)):
        for k in range(len(alfabet)):
            if kata1[i] == alfabet[k]:
                indeks_kata1[k] += 1
                break
    

    #memasukkan indeks dari kata2 ke indeks_kata2
    for i in range(len(kata2)):
        for j in range(len(alfabet)):
            if kata2[i] == alfabet[j]:
                indeks_kata2[j] += 1
                break
    #print(indeks_kata2)
    #print(indeks_kata1)
    # k = True
    # for i in range(len(alfabet)):
    #     if indeks_kata1[i][1] != indeks_kata2[i][1]:
    #         k = False 
    #         break
    
    # return k
    if indeks_kata1 == indeks_kata2:
        return True
    else:
        return False
    #return indeks_kata1 == indeks_kata2


#string_acak('aabccd')
#string_acak('alterra', 'terta')
print(string_acak('malang', 'agmlan'))
print(string_acak('alterra', 'rerlata'))
print(string_acak('alterra', 'terta'))
print(string_acak('python', 'nothyd'))
print(string_acak('python', 'nothyp'))
