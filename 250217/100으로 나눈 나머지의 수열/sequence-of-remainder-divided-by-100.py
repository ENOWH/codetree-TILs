N = int(input())

def Nth(n):
    if n==1:
        return 2
    elif n==2:
        return 4
    else:
        return (Nth(n-1)*Nth(n-2))%100

print(Nth(N))