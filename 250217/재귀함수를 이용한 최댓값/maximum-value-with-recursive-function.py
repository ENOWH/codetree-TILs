N = int(input())
arr = list(map(int, input().split()))

def maximum(n, array):
    if n==1:
        return array[n-1]
    else:
        if maximum(n-1, array)>array[n-1]:
            return maximum(n-1, array)
        else:
            return array[n-1]

print(maximum(N, arr))