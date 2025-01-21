n = int(input())

for _ in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    sum_val=0
    for i in range(a, b+1):
        if i%2==0:
            sum_val+=i
    print(sum_val)