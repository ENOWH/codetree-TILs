n = int(input())
array = list(map(int, input().split()))

n = len(array)

for i in range(n - 1):
    for j in range(n - i - 1):
        if array[j] < array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array[0], array[1])