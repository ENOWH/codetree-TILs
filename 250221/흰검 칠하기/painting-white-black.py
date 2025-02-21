OFFSET = 100000
MAX_R = 200000

n = int(input())
arr_color = [0 for _ in range(MAX_R+1)]
arr_cnt = [0 for _ in range(MAX_R+1)]

for _ in range(n):
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction == 'L':
        for j in range(0, -distance, -1):
            arr_color[OFFSET+j] = 'L'
            arr_cnt[OFFSET+j] +=1
        OFFSET -= (distance-1)

    elif direction == 'R':
        for j in range(distance):
            arr_color[OFFSET+j] = 'R'
            arr_cnt[OFFSET+j] +=1
        OFFSET += (distance-1)

white, black, gray = 0,0,0

for i in range(MAX_R+1):
    if arr_cnt[i]>=4:
        gray += 1
    elif arr_cnt[i] >= 1:
        if arr_color[i] == 'L':
            white += 1
        elif arr_color[i] == 'R':
            black += 1

print(white, black, gray)