n = int(input())

def summing(n):
    if n==1:
        return 1
    return n+summing(n-1)

print(summing(n))