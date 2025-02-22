MAX_R = 200
OFFSET = 100

n = int(input())
rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

checked = [[0 for _ in range(MAX_R+1)] for _ in range(MAX_R+1)]
for i, (x1, y1, x2, y2) in enumerate(rects):
    x1, y1, x2, y2 = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET
    if i%2==0:
        for x in range(x1, x2):
            for y in range(y1, y2):
                checked[x][y] = 'R'
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                checked[x][y] = 'B'

area_blue = 0
for x in range(MAX_R+1):
    for y in range(MAX_R+1):
        if checked[x][y] == 'B':
            area_blue += 1
print(area_blue)
