start, end = map(int, input().split())
cnt=0
# Write your code here!
for i in range(start, end+1):
    sum_val = 0
    for j in range(1,i):
        if i%j==0:
            sum_val+=j
    if i==sum_val:
        cnt += 1
print(cnt)