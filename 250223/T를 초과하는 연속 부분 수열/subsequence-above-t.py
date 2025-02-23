n, T = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans,cnt = 0,0
for i in range(n):
    if i>=1 and arr[i]>T and arr[i-1]>T:
        cnt += 1
    else:
        cnt = 1
    ans = max(ans, cnt)

print(ans)