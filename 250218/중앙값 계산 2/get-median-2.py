n = int(input())
list_arr = list(map(int, input().split()))
arr = []
sorted_arr = []

for i in range(n):
    arr.append(list_arr[i])
    
    if len(arr)%2==1:
        sorted_arr = sorted(arr)
        print(sorted_arr[len(arr)//2], end = " ")