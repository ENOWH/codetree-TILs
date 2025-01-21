n = int(input())

for i in range(n):
    for j in range(n):
        if i<=j and i!=0 and j!=n-1:
            print(" ", end = " ")
        else:
            print("*", end = " ")
    print()