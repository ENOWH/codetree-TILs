n = int(input())
cnt=0
arr=[]
i=0

while True:
    i+=1
    arr.append(n*i)
    if (n*i)%5 == 0:
        cnt+=1
    if cnt == 2:
        break

for elem in arr:
    print(elem, end = " ")