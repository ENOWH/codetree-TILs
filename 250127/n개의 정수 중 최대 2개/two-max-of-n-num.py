n = int(input())
array = list(map(int, input().split()))

n = len(array)

for i in range(1, n):
    for j in range(i, 0, -1):
        if array[j-1] < array[j]:
            array[j-1], array[j] = array[j], array[j-1]

print(array[0], array[1])