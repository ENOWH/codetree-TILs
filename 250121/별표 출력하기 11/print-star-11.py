n = int(input())

for i in range(2*n+1):
    if i%2==0:
        print("*", end = " ")
        for _ in range(n):
            print("*", end = " ")
            print("*", end = " ")
    else:
        print("*", end = " ")
        for _ in range(n):
            print(" ", end = " ")
            print("*", end = " ")
    print()