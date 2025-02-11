M, D = map(int, input().split())

def MD(M, D):
    if M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
        if D>=1 and D<=31:
            return True
    elif M==4 or M==6 or M==9 or M==11:
        if D>=1 and D<=30:
            return True
    elif M==2:
        if D>=1 and D<=28:
            return True
    else:
        return False
    return False

if MD(M, D):
    print("Yes")
else:
    print("No")