n, k, t = input().split()
n, k = int(n), int(k)
string = [input() for _ in range(n)]
string_t = []

for elem in string:
    if elem[:len(t)]==t:
        string_t.append(elem)

string_t.sort()
print(string_t[k-1])