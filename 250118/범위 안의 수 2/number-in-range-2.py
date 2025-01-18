sum_val=0
cnt=0

for _ in range(10):
    n = int(input())
    if n<=200 and n>=0:
        sum_val += n
        cnt+=1
print(f"{sum_val} {sum_val/cnt:.1f}")