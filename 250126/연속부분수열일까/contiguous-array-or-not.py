n1, n2 = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
satisfied = True

for i in range(len(arr_A)):
    if arr_A[i]==arr_B[0]:
        k=i
        break


for i in range(len(arr_B)):
    if arr_A[i+k]!=arr_B[i]:
        satisfied=False
        break

if satisfied==True:
    print("Yes")
else:
    print("No")