A = input()
B = input()
str_A = ''
str_B = ''

for elem in A:
    if elem >= '0' and elem <= '9':
        str_A += elem

for elem in B:
    if elem >= '0' and elem <= '9':
        str_B += elem

print(int(str_A)+int(str_B))