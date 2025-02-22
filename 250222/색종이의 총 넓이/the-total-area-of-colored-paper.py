n = int(input())
rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
OFFSET = 100
MAX_R = 200
checked = [[0 for _ in range(MAX_R)] for _ in range(MAX_R)]

for x, y in rects:
    x, y = x+OFFSET, y+OFFSET
    for i in range(x, x+8):
        for j in range(y, y+8):
            checked[i][j] = 1

area = 0
for x in range(MAX_R):
    for y in range(MAX_R):
        if checked[x][y] == 1:
            area += 1
print(area)