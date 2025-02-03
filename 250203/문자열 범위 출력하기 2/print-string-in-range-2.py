string = input()
n = int(input())

for i in range(len(string)-1, len(string)-n-1, -1):
    print(string[i], end = "")