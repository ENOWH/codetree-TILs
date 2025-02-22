n = int(input())
OFFSET = 100
MAX_R = 200

rectangle = [[0 for _ in range(MAX_R+1)] for _ in range(MAX_R+1)]

for _ in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            rectangle[OFFSET+i][OFFSET+j] = 1

count = 0
for i in range(MAX_R+1):
    for j in range(MAX_R+1):
        if rectangle[i][j] == 1:   
            count += 1
print(count)