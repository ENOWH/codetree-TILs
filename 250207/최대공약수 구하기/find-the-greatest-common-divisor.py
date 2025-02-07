n, m = map(int, input().split())

def greatest_common_divisor(n, m):
    lst = []
    for i in range(1, max(n,m)+1):
        if n%i == 0 and m%i == 0:
            lst.append(i)
    print(lst[-1])

greatest_common_divisor(n, m)