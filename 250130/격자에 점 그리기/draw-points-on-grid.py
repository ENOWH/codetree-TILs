n, m = tuple(map(int, input().split()))

placed = [
    [0 for _ in range(n)]
    for _ in range(n)
]
num = 1

for i in range(m):
    r, c = tuple(map(int, input().split()))
    placed[r-1][c-1] = num
    num += 1

for i in range(n):
    for j in range(n):
        print(placed[i][j], end = " ")
    print()