inp = input().split()
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])

if a>=b and a>=c:
    if b>=c:
        print(b)
    else:
        print(c)
elif b>=c and b>=a:
    if c>=a:
        print(c)
    else:
        print(a)
else:
    if b>=a:
        print(b)
    else:
        print(a)