n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# [0][0]
# [0][1], [1][0]
# [0][2], [1][1], [2][0]
# ...
# [0][5], ... [3][2]
# [1][5], [2][4], [3][3]
# [2][5], [3][4]
# [3][5]

k = 0
num = 1

while True:
    for i in range(k+1):
        if i<n and k-i<m:
            arr[i][k-i] = num
            num += 1
    k += 1

    if k > n+m-2:
        break    

for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()