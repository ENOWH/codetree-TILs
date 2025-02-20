m1, d1, m2, d2 = map(int, input().split())
days_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def nums_of_days(m, d):
    total_days = 0
    for i in range(1, m):
        total_days += days_of_month[i]
    total_days += d

    return total_days

diff = nums_of_days(m2, d2) - nums_of_days(m1, d1) + 1

ans = [0 for _ in range(8)]

for i in range(diff):
    i = i%7 + 1
    ans[i] += 1

s = input()

if s == 'Mon':
    print(ans[1])
elif s == "Tue":
    print(ans[2])
elif s == "Wed":
    print(ans[3])
elif s == "Thu":
    print(ans[4])
elif s == "Fri":
    print(ans[5])
elif s == "Sat":
    print(ans[6])
elif s == "Sun":
    print(ans[7])