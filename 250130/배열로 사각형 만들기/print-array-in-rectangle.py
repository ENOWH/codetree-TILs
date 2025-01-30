arr = [
    [1 for _ in range(5)]
    for _ in range(5)
]

for i in range(4):
    for j in range(4):
        arr[i+1][j+1] = arr[i+1][j]+arr[i][j+1]

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()