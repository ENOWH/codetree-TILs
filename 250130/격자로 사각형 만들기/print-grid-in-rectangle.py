n = int(input())

arr = [
    [1 for _ in range(n)]
    for _ in range(n)
]

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] + arr[i-1][j-1]

for row in range(n):
    for col in range(n):
        print(arr[row][col], end = " ")
    print()