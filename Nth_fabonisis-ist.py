n=int(input())
empty_list=[1,1]

while len(empty_list)<n:
    k = sum(empty_list[-2:])
    empty_list.append(k)
print(empty_list)
print(empty_list[-1])

