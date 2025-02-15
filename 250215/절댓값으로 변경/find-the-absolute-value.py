n = int(input())
arr = list(map(int, input().split()))

def modulus(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i]=-arr[i]
    return arr

modulus(arr)

for elem in arr:
    print(elem, end = " ")