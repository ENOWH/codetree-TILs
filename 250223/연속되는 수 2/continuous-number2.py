n = int(input())
arr = [int(input()) for _ in range(n)]
arr_number = []
arr_cnt = [1 for _ in range(1001)]

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        arr_cnt[arr[i]] += 1

print(max(arr_cnt)) 