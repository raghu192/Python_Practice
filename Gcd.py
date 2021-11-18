n1=int(input())
n2=int(input())
if n2>n1:
    n1,n2=n2,n1
while n1%n2!=0:
    rem=n1%n2
    n1=n2
    n2=rem
print('hcf equal to',n2)
