N = int(input())
array = list(map(int, input().split()))

def find_max(arr):
    if len(arr)==1:
        return arr[0]
    return max(arr[0], find_max(arr[1:]))

print(find_max(array))