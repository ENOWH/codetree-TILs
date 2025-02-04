A = input()
B = input()
cnt=0

for i in range(len(A)):
    if i + len(B) - 1 > len(A) - 1:
        continue
    
    if A[i:i+2] == B:
        cnt += 1
print(cnt)