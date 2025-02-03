string = input()
alphabet = input()

cnt = 0

for i in range(len(string)):
    if string[i]==alphabet:
        cnt+=1

print(cnt)