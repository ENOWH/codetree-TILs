MAX_R = 200000
OFFSET = 100000

n = int(input())
arr = [0 for _ in range(MAX_R+1)]

for _ in range(n):
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction == 'L':
        for j in range(0, -distance, -1):
            arr[OFFSET+j] = 'L'
        OFFSET -= (distance-1)
    else:
        for j in range(distance):
            arr[OFFSET+j] = 'R'
        OFFSET += (distance-1)
    
white, black = 0, 0
for i in range(MAX_R+1):
    if arr[i] == 'L':
        white += 1
    elif arr[i] == 'R':
        black += 1
print(white, black)