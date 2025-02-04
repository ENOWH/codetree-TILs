string, alphabet = input().split()

if alphabet in string:
    print(string.index(alphabet))
else:
    print("No")