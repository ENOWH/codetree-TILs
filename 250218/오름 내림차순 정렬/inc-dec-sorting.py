n = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(nums)
for elem in sorted_nums:
    print(elem, end = " ")
print()
reversed_nums = sorted_nums[::-1]
for elem in reversed_nums:
    print(elem, end = " ")