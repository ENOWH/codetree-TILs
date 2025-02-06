A = input()
B = input()
n = 0

while True:
    if A == B:
        print(n)
        break

    A = A[-1] + A[:-1]
    n += 1
    
    if n == len(A):
        print(-1)
        break