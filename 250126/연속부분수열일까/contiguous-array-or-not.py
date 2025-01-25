n1, n2 = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
satisfied = True

if n1<=n2:
    n1, n2 = n2, n1

for i in range(n1):
    if arr_A[i]==arr_B[0]:
        k=i
        break

for i in range(n2):
    if arr_A[k+i]!=arr_B[i]:
        satisfied=False

if satisfied==True:
    print("Yes")
else:
    print("No")