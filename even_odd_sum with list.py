N=input()
empty_list=[]
for i in N:
    empty_list.append(int(i))
odd_sum=0
even_sum=0
for value in empty_list:
    if value%2==0:
        even_sum=even_sum+value
    else:
     odd_sum=odd_sum+value
print(even_sum," ",odd_sum)