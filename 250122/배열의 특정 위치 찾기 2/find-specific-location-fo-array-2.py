arr = list(map(int, input().split()))
sum_even, sum_odd = 0,0

for i in range(10):
    if (i+1)%2==0:
        sum_even += arr[i]
    else:
        sum_odd += arr[i]

if sum_even>=sum_odd:
    print(sum_even-sum_odd)
else:
    print(sum_odd-sum_even)