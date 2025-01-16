inp = input().split()
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])

if a>=b:
    if c>=a:
        print(a)
    elif b>=c:
        print(b)
    else:
        print(c)
else:
    if c>=b:
        print(b)
    elif a>=c:
        print(a)
    else:
        print(c)
