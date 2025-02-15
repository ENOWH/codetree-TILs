N, M = tuple(map(int, input().split()))
A = list(map(int, input().split()))

def sum_(a, b, arr):
    sum_val = 0
    for i in range(a, b+1):
        sum_val+=arr[i-1]
    return sum_val

for _ in range(M):
    a1, a2 = tuple(map(int, input().split()))
    print(sum_(a1, a2, A))