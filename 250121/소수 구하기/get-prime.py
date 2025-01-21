n = int(input())

for num in range(1, n+1):
    divisor_cnt=0
    for divisor in range(1, num+1):
        if num%divisor==0:
            divisor_cnt+=1

    if divisor_cnt==2:
        print(num, end = " ")