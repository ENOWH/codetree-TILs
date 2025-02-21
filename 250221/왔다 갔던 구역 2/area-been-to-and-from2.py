n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

ans = [0 for _ in range(1001)]

for i in range(n):
    if dir[i] == "L":
        for j in range(x[i]):
            ans[j+500] += 1
    else:
        for j in range(x[i]):
            ans[j+500] += 1
    
cnt = 0
for i in range(len(ans)):
    if ans[i]>=2:
        cnt += 1
print(cnt)