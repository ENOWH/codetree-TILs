cnt=0
lst = []

while True:
    s = input()
    if s == '0':
        break
    else:
        cnt += 1
        if cnt%2 != 0:
            lst.append(s)
print(cnt)
for elem in lst:
    print(elem)