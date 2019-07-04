#fungsi yang lebih ringkas untuk cek sequence
def max_sum_list(arr):
    max = -float('inf')
    for i in range(len(arr)):
        sum = 0
        for j in arr[i:]:
            sum += j
            if sum > max:
                max = sum
    return max




#cek jumlah bilangan di arr
def cekjumlahbilanganarr(arr):
    jumlah = 0
    for i in range(len(arr)):
        jumlah += arr[i]
    return jumlah

#cek maksimum list
def cekmaksimumlist(arr):
    maks = arr[0]
    for i in range(len(arr)):
        if maks < arr[i]:
            maks = arr[i]
    return maks

def maxSequence(arr):
    simpanjumlah = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            simpanjumlah.append(cekjumlahbilanganarr(arr[i:j]))
    return cekmaksimumlist(simpanjumlah)


print(maxSequence([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSequence([-2,-5,6,-2,-3,1,5,-6]))
print(maxSequence([1000]))

print(max_sum_list([-2,1,-3,4,-1,2,1,-5,4]))
print(max_sum_list([-2,-5,6,-2,-3,1,5,-6]))
print(max_sum_list([1000]))