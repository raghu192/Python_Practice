N=input()
empty_list=[]
for i in N:
    empty_list.append(int(i))

k=empty_list.copy()
k.reverse()
if k==empty_list:
    print("palindrome")
else:
    print('not a palin drome')