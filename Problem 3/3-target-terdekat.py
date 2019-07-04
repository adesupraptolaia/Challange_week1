def targetTerdekat(arr):
    len_arr = len(arr)
    #list tempat indeks o dan x berada dimana aja 
    index_o = []
    index_x = []    
    #memasukkan indeks o dan x kedalam list
    for i in range(len_arr):
        if 'o' == arr[i]:
            index_o.append(i)
        if 'x' == arr[i]:
            index_x.append(i)
    
    # tentukan jarak terpendek
    if index_o == [] or index_x == []:
        return 0
    else:
        jarak = abs(index_o[0] - index_x[0])
        for i in index_o:
            for k in index_x:
                if jarak > abs(i-k):
                    jarak = abs(i-k)
    return jarak
                    

print(targetTerdekat(['','','o','','','x','','x']))

