N, M = tuple(map(int, input().split()))
A = list(map(int, input().split()))

def program(arr, num):
    sum_val = 0

    while num>=1:
        sum_val += arr[num-1]
        if num%2==1:
            num-=1
        else:
            num//=2
    return sum_val

print(program(A, M))