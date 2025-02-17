n = int(input())

def ruling(n):
    if n==1:
        return 0
    if n%2==0:
        return ruling(n//2)+1
    else:
        return ruling(3*n+1)+1

print(ruling(n))