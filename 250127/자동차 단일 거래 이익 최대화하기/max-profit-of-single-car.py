n = int(input())
price = list(map(int, input().split()))

max_val = 0

for i in range(n-1):
    for j in range(i+1, n):
        if max_val < price[j]-price[i]:
            max_val = price[j]-price[i]

print(max_val)