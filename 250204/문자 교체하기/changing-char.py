A, B = input().split()

s = A[:2]

B = list(B)

B[:2] = A[:2]

B = "".join(B)

print(B)