n=int(input())
i=1
while i<=n:
    j=1
    strt_patt=chr(ord('A')+i-1)
    while j<=n:
        chrp=chr(ord(strt_patt)+j-1)
        print(chrp,end='')
        j=j+1
    print()
    i=i+1




