A = input()

for elem in A:
    if elem >= 'A' and elem <= 'Z':
        print(chr(ord(elem) - ord('A') + ord('a')), end = "")
    elif elem >= 'a' and elem <= 'z':
        print(chr(ord(elem) - ord('a') + ord('A')), end = "")
