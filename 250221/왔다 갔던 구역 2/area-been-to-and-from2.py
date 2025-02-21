N = int(input())

arr = [0 for _ in range (1001)]
offset = 500

for i in range(N):
    go, cmd = map(str, input().split())
    go = int(go)

    if cmd == 'R':
        for j in range(go):
            arr[offset + j] += 1
        offset += go

    if cmd == 'L':
        for j in range(1, go+1):
            arr[offset - j] += 1
        offset -= go

count = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        count += 1
        
print(count)