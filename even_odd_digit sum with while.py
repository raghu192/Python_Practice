n= int(input())
eve_sum=0
odd_sum=0
while n!=0:
    quo=n//10
    rem=n%10
    if rem%2==0:
        eve_sum=eve_sum+rem
    else:
        odd_sum=odd_sum+rem
    n=quo
print(eve_sum," ",odd_sum)
