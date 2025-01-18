a,b=input().split()
a,b=int(a),int(b)

prod=1
for _ in range(b):
    prod*=a
print(prod)