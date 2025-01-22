arr = list(map(int, input().split()))
count_arr = [0 for _ in range(10)]

for elem in arr:
    if elem>=10 and elem<=99:
        count_arr[elem//10]+=1

for i in range(1, 10):
    print(i, "-", count_arr[i])