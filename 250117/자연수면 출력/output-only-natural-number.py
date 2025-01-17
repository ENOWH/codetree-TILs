a, b = input().split()
a, b = int(a), int(b)

if a > 0:
    for _ in range(b):
        print(a, end = "")
else:
    print(0)