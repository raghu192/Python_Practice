n=int(input())
i=0
j=1
mark=False
while (i+j)<=n:
    k=i+j
    if k==n:
        mark=True
    i=j
    j=k
    i+j
if mark:
    print(" N is part of fabonosisi series")
else:
    print(" N is not a part of fabonosisi series")
