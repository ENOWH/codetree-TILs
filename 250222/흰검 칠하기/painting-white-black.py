OFFSET = 100000
MAX_R = 200000

n = int(input())
arr_L = [0 for _ in range(MAX_R+1)]
arr_R = [0 for _ in range(MAX_R+1)]
arr = [0 for _ in range(MAX_R+1)]

cur = OFFSET
for _ in range(n):
    pivot, direction = tuple(input().split())
    pivot = int(pivot)

    if direction == 'L':
        while pivot>0:
            arr[cur] = 'L'
            arr_L[cur] += 1
            pivot -= 1
            if pivot:
                cur -= 1

    else:
        while pivot>0:
            arr[cur] = 'R'
            arr_R[cur] += 1
            pivot -= 1
            if pivot:
                cur += 1

white, black, gray = 0,0,0

for i in range(MAX_R+1):
    if arr_L[i]>=2 and arr_R[i]>=2:
        gray += 1
    elif arr[i] == 'L':
        white += 1
    elif arr[i] == 'R':
        black += 1
print(white, black, gray)