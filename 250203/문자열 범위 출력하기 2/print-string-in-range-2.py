string = input()
n = int(input())

length = len(string)
cnt = 0

for i in range(length-1, -1, -1):
    print(string[i], end ="")
    cnt += 1
    if cnt > n:
        break