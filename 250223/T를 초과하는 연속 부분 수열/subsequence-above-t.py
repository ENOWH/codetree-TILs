n, T = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans,cnt = 0,0
for i in range(n):
    if arr[i]>T:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)

print(ans)