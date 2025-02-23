n = int(input())
arr = [int(input()) for _ in range(n)]
result = 0
cnt = 0

for i in range(1, n):
    if arr[i] == arr[i-1]:
        cnt += 1
    else:
        result = max(cnt, result)
        cnt = 0
    result = max(cnt, result)
print(result+1)