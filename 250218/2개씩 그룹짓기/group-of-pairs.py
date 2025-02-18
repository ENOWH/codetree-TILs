n = int(input())
nums = list(map(int, input().split()))

group_max = 0
nums.sort()

for i in range(n):
    if nums[i]+nums[2*n-1-i]>group_max:
        group_max = nums[i]+nums[2*n-1-i]

print(group_max)