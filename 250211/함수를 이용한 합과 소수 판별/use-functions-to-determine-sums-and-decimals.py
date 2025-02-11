a, b = map(int, input().split())

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def even(n):
    n = str(n)
    sum_val = 0
    for elem in n:
        sum_val += int(elem)
    if sum_val%2 == 0:
        return True
    return False

cnt=0
for i in range(a, b+1):
    if is_prime(i) and even(i):
        cnt+=1
print(cnt)