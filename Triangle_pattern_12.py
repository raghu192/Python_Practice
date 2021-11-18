
n=int(input())
if n==1:
    char='A'
elif n==2:
    char='B'
elif n==3:
    char='C'
elif n==4:
    char='D'
elif n==5:
    char='E'
elif n==6:
    char='F'
elif n==7:
    char='G'
elif n==8:
    char='H'
elif n==9:
    char='I'
elif n==10:
    char='J'
elif n==11:
    char='K'
elif n==12:
    char='L'
elif n==13:
    char='M'
elif n==14:
    char='N'
elif n==15:
    char='O'
elif n==16:
    char='P'
elif n==17:
    char='Q'
elif n==18:
    char='R'
elif n==19:
    char='S'
elif n==20:
    char='T'
elif n == 21:
    char = 'U'
elif n==22:
    char='V'
elif n==23:
    char='W'
elif n==24:
    char='X'
elif n==25:
    char='Y'
elif n==26:
    char='Z'



i = 1

while i <= n:
    j = 1
    start_char= chr(ord(char))
    p=start_char
    while j <= i:
        if j==i:
            print(p, end='')
        else:
            print(chr(ord(start_char)-i+1),end='')
        j = j + 1
        start_char=chr(ord(start_char)+1)
    print()
    i = i + 1
