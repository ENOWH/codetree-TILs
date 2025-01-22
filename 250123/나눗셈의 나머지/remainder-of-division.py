arr = [0]*10
a, b = map(int, input().split())

while a>=1:
    a//=b
    remainder = a%b
    for i in range(10):
        if remainder==i:
            arr[i]+=1

sum_val=0

for i in range (10):
    sum_val+=(arr[i]*arr[i])
print(sum_val)