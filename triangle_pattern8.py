n = int(input())
i = 1
while i <= n:
    j = i
    while j <= i and j >= 1:
        print(j, end='')
        j = j - 1

    print()
    i = i + 1
