arr = tuple(input().split())
length=0
for elem in arr:
    length += len(elem)
print(length)