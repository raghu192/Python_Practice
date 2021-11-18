n=int(input())
i=1
j=1
counter=3
if n==1:
        print(i)
elif n==2:
        print(j)
else:
        while counter<=n and (i+j)>0:

                k=i+j

                i=j
                j=k
                i+j
                counter=counter+1
        print(k)