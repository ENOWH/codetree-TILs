N = int(input())

def program(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return program(n//3) + program(n-1)
print(program(N))