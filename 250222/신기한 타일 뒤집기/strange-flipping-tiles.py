MAX_R = 200000
OFFSET = 100000

n = int(input())
arr = [0 for _ in range(MAX_R+1)]

cur = OFFSET
for _ in range(n):
    count, direction = tuple(input().split())
    count = int(count)

    if direction == 'L':
        while count>0:
            arr[cur] = 'L'
            count -= 1
            if count:
                cur -= 1
    else:
        while count>0:
            arr[cur] = 'R'
            count -= 1
            if count:
                cur += 1
    
white, black = 0, 0
for i in range(MAX_R+1):
    if arr[i] == 'L':
        white += 1
    elif arr[i] == 'R':
        black += 1
print(white, black)