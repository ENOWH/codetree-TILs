n = int(input())

sum_val=0
for _ in range(n):
    N = int(input())
    if N%2==1 and N%3==0:
        sum_val+=N
print(sum_val)