def perkalianUnik(arr):
    jumlah = 1
    arr1 = []
    for i in range(len(arr)):
        jumlah = jumlah*arr[i]
    for i in range(len(arr)):
        jumlah1 = int(jumlah/arr[i])
        arr1.append(jumlah1)
    return arr1

print(perkalianUnik([2, 4, 6]))
print(perkalianUnik([1, 2, 3, 4, 5]))
print(perkalianUnik([1, 4, 3, 2, 5]))
print(perkalianUnik([1, 3, 3, 1]))
print(perkalianUnik([2,1,8, 10, 2]))

