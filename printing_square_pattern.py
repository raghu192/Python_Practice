n = int(input())  # n0.0f .rows
i = 1 # row counter
while i <= n:
    j = 1 # coloumn counter
    while j <= n:
        print(n, end='') #end with empty character with no automatic enter
        j = j + 1  #incrementing coloumn
    print()
    i = i + 1      #incrementing row
