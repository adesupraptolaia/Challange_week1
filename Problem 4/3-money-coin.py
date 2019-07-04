def convertToCoin(duit):
        kembalian = []
        duit_pecahan = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 1]
        for i in range(len(duit_pecahan)):
            while(duit >= duit_pecahan[i]):
                kembalian.append(duit_pecahan[i])
                duit -= duit_pecahan[i]
        return kembalian

print(convertToCoin(543))
print(convertToCoin(7752))
print(convertToCoin(37454))
