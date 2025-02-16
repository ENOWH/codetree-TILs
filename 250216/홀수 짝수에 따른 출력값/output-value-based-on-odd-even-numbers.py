N = int(input())

def summing_odd(n):
    if n==1:
        return 1
    return summing_odd(n-2)+n
    
def summing_even(n):
    if n==2:
        return 2
    return summing_even(n-2)+n

if N%2==0:
    print(summing_even(N))
else:
    print(summing_odd(N))