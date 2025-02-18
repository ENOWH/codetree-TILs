n = int(input())
word = [input() for _ in range(n)]

word = sorted(word)
for elem in word:
    print(elem)