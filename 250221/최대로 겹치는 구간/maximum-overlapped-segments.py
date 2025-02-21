n = int(input())
ans = [0] * 300

for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))

    for i in range(x1+100, x2+100):
        ans[i] += 1
    
print(max(ans))