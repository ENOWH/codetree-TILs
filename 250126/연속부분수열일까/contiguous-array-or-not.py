n1, n2 = map(int, input().split())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
satisfied = False

for i in range(len(arr_A)):
    if arr_A[i:i+len(arr_B)]==arr_B[i]:
        satisfied = True

if satisfied==True:
    print("Yes")
else:
    print("No")