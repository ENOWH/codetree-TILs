a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
satisfied=True

for i in range(a, b+1):
    if i%c==0:
        satisfied=False

if satisfied == False:
    print("NO")
else:
    print("YES")