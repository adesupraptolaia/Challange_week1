def cariMedian(arr):
    panjang = len(arr)
    if panjang % 2 == 0:
        t = int(panjang/2)
        if (arr[t]+arr[t-1]) % 2 == 0:
            return int((arr[t]+arr[t-1])/2)
        else:
            return (arr[t]+arr[t-1])/2
        
    else:
        t = int((panjang+1)/2)
        return arr[t-1]

print(cariMedian([1,2,3,4,5]))
print(cariMedian([1,3,4,10,12,13]))
print(cariMedian([3,4,7,6,10]))
print(cariMedian([1,3,3]))
print(cariMedian([7,7,8,8]))