n = int(input())
arr = list(map(int, input().split()))

list_ = [elem**2 for elem in arr]

for elem in list_:
    print(elem, end = " ")