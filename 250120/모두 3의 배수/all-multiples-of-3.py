satisfied=True
cnt=0

while True:
    cnt+=1
    n = int(input())
    if n%3!=0:
        satisfied=False
    if cnt>=5:
        break

if satisfied==True:
    print("1")
else:
    print("0")