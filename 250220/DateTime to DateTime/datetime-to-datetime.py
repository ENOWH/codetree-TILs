a, b, c = map(int, input().split())

def time_to_mins(d, h, m):
    d = 24*60*d
    h = 60*h
    total_mins = d+h+m
    return total_mins

if a<11:
    print(-1)
elif a==11 and b<11:
    print(-1)
elif a==11 and b==11 and c<11:
    print(-1)
else:
    print(time_to_mins(a, b, c)-time_to_mins(11, 11, 11))