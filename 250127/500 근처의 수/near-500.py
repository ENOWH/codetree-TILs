arr = list(map(int, input().split()))
arr_A = []
arr_B = []

for i in range(10):
    arr[i] = arr[i] - 500

for i in range(10):
    if arr[i]>0:
        arr_A.append(arr[i])
    elif arr[i]<0:
        arr_B.append(arr[i])

min_val = arr_A[0]
for elem in arr_A:
    if elem < min_val:
        min_val = elem
        
max_val = arr_B[0]
for elem in arr_B:
    if elem > max_val:
        max_val = elem    

print(max_val+500, min_val+500)