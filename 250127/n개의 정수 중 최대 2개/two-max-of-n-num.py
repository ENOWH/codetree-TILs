n = int(input())
arr = list(map(int, input().split()))

if arr[0]>arr[1]:
		max1, max2 = arr[0], arr[1]
else:
		max2, max1 = arr[0], arr[1]
		
for i in range(2, n):
		if arr[i] >= max1:
				max2 = max1
				max1 = arr[i]
		elif arr[i] >= max2:
				max2 = arr[i]
				
print(max1, max2)