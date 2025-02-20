n = int(input())
arr = list(map(int, input().split()))

indexed_arr = [(val, idx) for idx, val in enumerate(arr)]
indexed_arr.sort()

position = [0 for _ in range(n)]

for new_idx, (_, original_idx) in enumerate(indexed_arr):
    position[original_idx] = new_idx+1

for elem in position:
    print(elem, end = " ")