n=int(input())
i=1
while i<=n:
    j=1
    while j<=n:
        chrp=chr(ord('A')+j-1)
        print(chrp,end='')
        j=j+1
    print()
    i=i+1




