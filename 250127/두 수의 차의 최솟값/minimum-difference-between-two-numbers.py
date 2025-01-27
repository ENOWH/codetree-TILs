n = int(input())
arr = list(map(int, input().split()))

min_val = arr[1]-arr[0]

for i in range(n-1):
    for j in range(i+1, n):
        if min_val > arr[j]-arr[i]:
            min_val = arr[j]-arr[i]

print(min_val)