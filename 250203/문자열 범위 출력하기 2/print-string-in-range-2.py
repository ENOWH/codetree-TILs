string = input()
n = int(input())

for i in range(n):
    print(string[len(string)-1-i], end = "")