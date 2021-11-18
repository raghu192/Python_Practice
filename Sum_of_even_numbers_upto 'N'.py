n=int(input())
i=1   # used for number increment
sum=0  # to store final sum value.Intially assigned it zero
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1
print("sum of even numbers upto N is",sum)
