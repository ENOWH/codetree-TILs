cnt=0
while True:
    n = int(input())
    if n%2==1:
        cnt+=1
    elif n%2==0:
        print(n//2)
        cnt+=1
    elif cnt==3:
        break