a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

for i in range(a, b+1):
    if i%c==0:
        satisfied = True
if satisfied==True:
    print("YES")
else:
    print("NO")