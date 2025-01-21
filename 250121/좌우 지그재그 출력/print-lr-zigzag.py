n = int(input())
cnt=1

for i in range(n):
    for j in range(n):
        if i%2==0:
            print(cnt, end = " ")
            if j!=n-1:
                cnt+=1
            else:
                cnt+=n
        else:
            print(cnt, end = " ")
            if j!=n-1:
                cnt-=1
            else:
                cnt+=n
    print()