n, q = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

for _ in range(q):
    arr = list(map(int, input().split()))
    num = arr[0]
    a = arr[1]
    if num == 1:
        print(nums[a-1])
    elif num == 2:
        print(nums.index(a)+1)
    elif num == 3:
        b = arr[2]
        for i in range(a, b+1):
            print(nums[i-1], end = " ")
        print()