n = int(input())
ans = [0]*101

for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))
    for i in range(x1, x2+1):
        ans[i] += 1

print(max(ans))