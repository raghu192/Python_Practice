n=int(input())
i=1
while i<=n:
    j=1
    strt_char_patt=chr(ord('A')+i-1)
    while j<=i:
        chrp=chr(ord(strt_char_patt))
        print(chrp,end='')
        j=j+1
    print()
    i=i+1
