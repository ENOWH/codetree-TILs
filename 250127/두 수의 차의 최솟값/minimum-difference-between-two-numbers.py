n = int(input())
arr = list(map(int, input().split()))

min_val = abs(arr[0]-arr[1])

for i in range(n-1):
    for j in range(i+1, n):
        if min_val > abs(arr[i] - arr[j]):
            min_val = abs(arr[i] - arr[j])

print(min_val)