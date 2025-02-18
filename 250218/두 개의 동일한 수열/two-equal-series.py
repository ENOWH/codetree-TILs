n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def equal(a, b):
    for elem1, elem2 in zip(a, b):
        if elem1 != elem2:
            return False
    return True

A.sort(); B.sort()

if equal(A, B):
    print("Yes")
else:
    print("No")