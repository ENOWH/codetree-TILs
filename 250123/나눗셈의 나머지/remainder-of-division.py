arr = [0]*10
a, b = map(int, input().split())

while a>1:
    for i in range(10):
        if i==a%b:
            arr[i]+=1
    a//=b

sum_val=0
for elem in arr:
    sum_val+=(elem**2)
print(sum_val)