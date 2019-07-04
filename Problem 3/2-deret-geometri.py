def tentukanDeretGeometri(arr):
    hasil = True
    banyak_bil = len(arr)
    if (banyak_bil<3):
        return "Deret yang anda masukkan salah!"
    else:
        for i in range(2,banyak_bil):
            if arr[i]*arr[i-2] != arr[i-1]**2:
                hasil = False
                break
    return hasil       

print(tentukanDeretGeometri([1, 3, 9, 27, 81]))
print(tentukanDeretGeometri([2, 4, 8, 16, 32]))
print(tentukanDeretGeometri([2,4,6,8]))
print(tentukanDeretGeometri([2,6,18,54]))
print(tentukanDeretGeometri([1,2,3,4,7,9]))

