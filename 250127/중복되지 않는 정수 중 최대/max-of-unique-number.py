n = int(input())
nums = list(map(int, input().split()))

new_nums = [0]*n

for i in range(n):
    if nums.count(nums[i])==1:
        new_nums.append(nums[i])

max_val=new_nums[0]
for i in range(n):
    for elem in new_nums:
        if elem >= max_val:
            max_val = elem

if new_nums == [0]*n:
    print(-1)
else:
    print(max_val)