n = int(input())
i = 1

while i <= n:
    j = 1
    p=n
    while j <= i:
        if j==i:
            print(n, end='')
        else:
            print(p-i+1,end='')
        j = j + 1
        p=p+1
    print()
    i = i + 1
