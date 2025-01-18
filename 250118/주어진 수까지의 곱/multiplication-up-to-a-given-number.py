a, b = input().split()
a, b = int(a),int(b)
prod=1
for i in range(a, b+1):
    prod*=i
print(prod)