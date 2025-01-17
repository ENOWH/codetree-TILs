a, b = input().split()
a, b = int(a), int(b)

i=a
while i<=b:
    if i%2==1:
        print(i, end = " ")
        i*=2
    else:
        print(i, end = " ")
        i+=3