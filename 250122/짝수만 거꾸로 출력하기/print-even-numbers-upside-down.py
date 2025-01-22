n = int(input())
arr = list(map(int, input().split()))
arr_even=[]

for elem in arr:
    if elem%2==0:
        arr_even.append(elem)
    
for elem in arr_even[::-1]:
    print(elem, end = " ")