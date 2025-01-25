n,m=tuple(map(int, input().split()))
arr = list(map(int, input().split()))
cnt = 0

for char in arr:
    if char == m:
        cnt+=1
print(cnt)