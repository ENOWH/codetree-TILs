N = int(input())
arr = [int(input()) for _ in range(N)]

ans, cnt = 0, 0
for i in range(N):
    if i>=1 and (arr[i]>=0 and arr[i-1]>=0) or (arr[i]<0 and arr[i-1]<0):
        cnt += 1
    else:
        cnt = 1
    ans = max(cnt, ans)
print(ans)