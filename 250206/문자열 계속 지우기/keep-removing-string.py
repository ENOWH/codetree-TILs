A = input()
B = input()

len_A = len(A)
len_B = len(B)

while True:
    inspection = 0
    for i in range(len_A-len_B+1):
        if A[i:i+len_B] == B:
            A = A[:i] + A[i+len_B:]
            len_A = len_A - len_B
            inspection += 1
    
    if inspection == 0:
        break
    
print(A)