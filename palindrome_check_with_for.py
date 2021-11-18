n=int(input())
rev=0
t=n #temporary varible
while t!=0:
    quo=t//10
    rem=t%10
    rev=(rev*10)+rem
    t=quo
print(rev)
if rev==n:
    print('yes')
else:
    print('no')