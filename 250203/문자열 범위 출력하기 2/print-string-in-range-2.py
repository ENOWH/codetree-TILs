string = input()
n = int(input())

if n >= len(string):
    for i in range(len(string)-1, len(string)-n-1, -1):
        print(string[i], end = "")
else:
    for elem in string:
        print(elem, end = "")