a, b = map(int, input().split())

def judge_369(num):
    num = str(num)
    judge = False
    for elem in num:
        if elem == '3' or elem == '6' or elem == '9':
            judge = True
    return judge

def multiples(num):
    return num%3 == 0

def is_magic_number(num):
    return judge_369(num) or multiples(num)

cnt = 0
for i in range(a, b+1):
    if is_magic_number(i):
        cnt += 1
print(cnt)