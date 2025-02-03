n = int(input())
cnt = 0
length = 0

for _ in range(n):
    string = input()
    length += len(string)

    if string[0]=="a":
        cnt+=1
print(length, cnt)
