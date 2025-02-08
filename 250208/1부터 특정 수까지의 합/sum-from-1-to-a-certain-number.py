n = int(input())

def sum_val_divided_10(n):
    sum_val = 0
    for i in range(1,n+1):
        sum_val += i
    return sum_val//10

print(sum_val_divided_10(n))