n, k = tuple(map(int, input().split()))
ans = [0 for _ in range(n+1)]

for _ in range(k):
    a, b = tuple(map(int, input().split()))
    for i in range(a, b+1):
        ans[i] += 1

print(max(ans))