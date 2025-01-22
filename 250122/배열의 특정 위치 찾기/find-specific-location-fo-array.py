arr = list(map(int, input().split()))

print(sum(arr[1::2]), sum(arr[2::3])/3)