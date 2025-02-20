m1, d1, m2, d2 = map(int, input().split())
days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def nums_of_days(m, d):
    total_days = 0
    for i in range(1, m):
        total_days += days_of_month[i]
    total_days += d
    return total_days


days1 = nums_of_days(m1, d1)
days2 = nums_of_days(m2, d2)

diff = days2 - days1
print(diff)
if diff>=0:
    print(day_of_the_week[diff%7+1])
else:
    print(day_of_the_week[-(-diff%7)+1])