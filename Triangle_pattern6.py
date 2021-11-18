n = int(input())
i = n
while i > 0:
    j = i

    while j <= i and j>0:
        print(j, end='')
        j = j - 1
    print()
    i = i-1