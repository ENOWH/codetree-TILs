n = int(input())
string = [
    input()
    for _ in range(n)
]
alphabet = input()
length = 0
cnt = 0

for elem in string:
    if elem[0]==alphabet:
        length += len(elem)
        cnt += 1

print(cnt, f"{length/cnt:.2f}")