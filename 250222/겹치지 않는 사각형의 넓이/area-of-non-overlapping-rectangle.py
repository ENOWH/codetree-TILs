rects = [
    tuple(map(int, input().split()))
    for _ in range(2)
]
OFFSET = 1000
MAX_R = 2000
checked = [[0 for _ in range(MAX_R+1)] for _ in range(MAX_R+1)]

for x1, y1, x2, y2 in rects:
    x1, y1, x2, y2, = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] = 1
    
x1, y1, x2, y2 = tuple(map(int, input().split()))
x1, y1, x2, y2, = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET
for x in range(x1, x2):
    for y in range(y1, y2):
        checked[x][y] = 0

area = 0 
for x in range(MAX_R+1):
    for y in range(MAX_R+1):
        if checked[x][y] == 1:
            area += 1
print(area)