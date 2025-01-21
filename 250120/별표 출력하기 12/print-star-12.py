n = int(input())

for i in range(n):
    for j in range(n):
        if i<=j:
            if j%2==0 and i!=0:
                print(" ", end = " ")
            else:
                print("*", end = " ")
        else:
            print(" ", end = " ")
    print()