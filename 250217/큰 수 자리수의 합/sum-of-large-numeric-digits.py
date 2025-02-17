a, b, c = map(int, input().split())
result = a*b*c

def summing(n):
    if n<10:
        return n
    return summing(n//10)+n%10

print(summing(result))