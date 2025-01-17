a, n = input().split()
a, n = int(a), int(n)

a += n
for _ in range(n):
    print(a)
    a += n