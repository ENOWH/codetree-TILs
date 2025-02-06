a, b = map(int, input().split())

sum_val = a+b
sum_val = str(sum_val)
cnt = 0

for elem in sum_val:
    if elem == '1':
        cnt += 1
print(cnt)