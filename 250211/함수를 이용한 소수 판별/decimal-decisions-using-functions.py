a, b = map(int, input().split())

def is_prime(n):
    for i in range(2, n-1):
        if n%i == 0:
            return False
    return True

sum_val = 0

for i in range(a, b+1):
    if is_prime(i):
        sum_val += i

print(sum_val)