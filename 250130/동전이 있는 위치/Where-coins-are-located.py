n, m = tuple(map(int, input().split()))

placed = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    placed[r][c] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(placed[i][j], end = " ")
    print()