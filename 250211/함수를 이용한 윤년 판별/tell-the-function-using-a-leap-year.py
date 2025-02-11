y = int(input())

def leap_year(n):
    if n%100 == 0 and n%400 != 0:
        return False
    elif n%4 == 0:
        return True
    else:
        return False

if leap_year(y):
    print("true")
else:
    print("false")