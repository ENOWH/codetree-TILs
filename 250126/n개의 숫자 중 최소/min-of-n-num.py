n = int(input())
a = list(map(int, input().split()))

min_val = a[0]
cnt = 1

for i in range(n):
    if min_val > a[i]:
        min_val = a[i]
        cnt = 1
    elif min_val == a[i]:
        cnt += 1

print(min_val, cnt)