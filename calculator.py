n= int(input())
while n>0:
    if n < 6 and n > 0:
        n1 = int(input())
        n2 = int(input())
    if n == 1:
        print(n1 + n2)
    elif n == 2:
        print(n1 - n2)
    elif n == 3:
        print(n1 * n2)
    elif n == 4:
        print(int(n1 / n2))
    elif n == 5:
        print(n1 % n2)
    elif n == 6:
        break
    else:
        print("Invalid Operation")
    n = int(input())
