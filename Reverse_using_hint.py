n=int(input())
rev=0
while n!=0:
    quo=n//10
    rem=n%10
    rev=(rev*10)+rem
    n=quo
print(rev)