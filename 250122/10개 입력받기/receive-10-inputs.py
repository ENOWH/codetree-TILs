arr = list(map(int, input().split()))
sum_val,cnt = 0,0

for elem in arr:
    if elem==0:
        break
    sum_val+=elem
    cnt+=1

print(f"%d %.1f" % (sum_val, sum_val/cnt))