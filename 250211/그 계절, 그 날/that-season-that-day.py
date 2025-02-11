Y, M, D = map(int, input().split())

def leap_year(n):
    if n%100==0 and n%400!=0:
        return False
    elif n%4==0:
        return True
    else:
        return False

def season(m):
    if m>=3 and m<=5:
        return "Spring"
    elif m>=6 and m<=8:
        return "Summer"
    elif m>=9 and m<=11:
        return "Fall"
    elif m==12 or m==1 or m==2:
        return "Winter"

def exist(y, m, d):
    if leap_year(y):
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            if d>=1 and d<=31:
                return True
        elif m==4 or m==6 or m==9 or m==11:
            if d>=1 and d<=30:
                return True
        elif m==2:
            if d>=1 and d<=29:
                return True
        else:
            return False
    else:
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            if d>=1 and d<=31:
                return True
        elif m==4 or m==6 or m==9 or m==11:
            if d>=1 and d<=30:
                return True
        elif m==2:
            if d>=1 and d<=28:
                return True
        else:
            return False

if exist(Y, M, D):
    print(season(M))
else:
    print(-1)