given_arr = map(int, input().split())
arr = []

for elem in given_arr:
    if elem == 0:
        break
    arr.append(elem)

for elem in arr[::-1]:
    print(elem, end=" ")