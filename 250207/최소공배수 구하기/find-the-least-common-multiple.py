n, m = map(int, input().split())

def least_common_multiple(n, m):
    lcm = 0
    while True:
        lcm += 1
        if lcm%n == 0 and lcm%m == 0:
            print(lcm)
            break

least_common_multiple(n, m)