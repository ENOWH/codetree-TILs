OFFSET = 100000
MAX_R = 200000

n = int(input())
arr_L = [0 for _ in range(MAX_R+1)]
arr_R = [0 for _ in range(MAX_R+1)]
arr = [0 for _ in range(MAX_R+1)]

for _ in range(n):
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction == 'L':
        for j in range(0, -distance, -1):
            arr[OFFSET+j] = 'L'
            arr_L[OFFSET+j] += 1
        OFFSET -= (distance-1)

    elif direction == 'R':
        for j in range(distance):
            arr[OFFSET+j] = 'R'
            arr_R[OFFSET+j] += 1
        OFFSET += (distance-1)

white, black, gray = 0,0,0

for i in range(MAX_R+1):
    if arr_L[i]>=2 and arr_R[i]>=2:
        gray += 1
    elif arr_L[i]>=1 or arr_R[i]>=1:
        if arr[i] == 'L':
            white += 1
        else:
            black += 1
print(white, black, gray)