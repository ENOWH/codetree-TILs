cnt = 0
while True:
    n = int(input())
    if n%2==1:
        pass
    elif n%2==0:
        cnt+=1
        print(n//2)
    if cnt>3:
        break