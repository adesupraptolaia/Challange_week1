n = 5

print("pattern 1")
for i in range(1,n+1):
    k = "* " * i
    print(k)

print("pattern 2")
for i in range(1, n+1):
    s = " " * (n-i)
    k = "* " * i
    print(s+k)

print("Pattern 3")
for i in range(1, n+1):
    l=""
    for k in range(i):
       l += str(k+1)
       l += " " 
    print(l)

print("pattern 4")
m = 1
for i in range(1,n+1):
    l=""
    for k in range(i):
        l += str(m)
        l += " "
        m += 1
    print(l)

print("pattern 5")
for i in range(1, n+1):
    s = " " * (n-i)
    k = "*" * i
    print(s+k)

