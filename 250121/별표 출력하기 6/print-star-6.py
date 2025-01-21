n = int(input())

for i in range(2*n-1):
    if i<n:
        for _ in range(i):
            print(" ", end = " ")
        for _ in range(2*n-2*i-1):
            print("*", end = " ")
        print()
    else:
        for _ in range(2*(n-1)-i):
            print(" ", end = " ")
        for _ in range(2*n-2*(2*(n-1)-i)-1):
            print("*", end = " ")
        print()