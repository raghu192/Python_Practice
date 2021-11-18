n1=int(input())
n2=int(input())
if n1>n2:
    while (n1%n2!=0):
        rem=n1%n2
        n1=n2
        n2=rem
    print(" gcd is",n2)
elif n2>n1:
    while (n2%n1!=0):
        rem=n2%n1
        n2=n1
        n1=rem
    print(" gcd is",n1)