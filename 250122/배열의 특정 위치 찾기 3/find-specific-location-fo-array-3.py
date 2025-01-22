arr = list(map(int, input().split()))
cnt, sum_val = 0, 0

for elem in arr:
    if elem != 0:
        cnt += 1
    else:
        break

print(arr[cnt-1]+arr[cnt-2]+arr[cnt-3])