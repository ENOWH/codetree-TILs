MAX_R = 2000
OFFSET = 1000

rects = [
    tuple(map(int, input().split()))
    for _ in range(2)
]

checked = [[0 for _ in range(MAX_R+1)] for _ in range(MAX_R+1)]
for i, (x1, y1, x2, y2) in enumerate(rects, start = 1):
    x1, y1, x2, y2 = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET
    for x in range(x1, x2):
        for y in range(y1, y2):
            checked[x][y] = i

list_x = []
list_y = []
for x in range(MAX_R+1):
    for y in range(MAX_R+1):
        if checked[x][y] == 1:
            list_x.append(x)
            list_y.append(y)
            
print(((max(list_x)-min(list_x))+1)*((max(list_y)-min(list_y))+1))