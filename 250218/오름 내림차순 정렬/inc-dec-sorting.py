n = int(input())
nums = list(map(int, input().split()))

nums.sort()
for elem in nums:
    print(elem, end = " ")
nums.sort(reverse=True)
print()
for elem in nums:
    print(elem, end = " ")