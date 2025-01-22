n = int(input())
arr = [1, n]

for i in range(2,100):
    arr_ = arr[i-1]+arr[i-2]
    arr.append(arr_)
    if arr_>100:
        break

for elem in arr:
    print(elem, end = " ")