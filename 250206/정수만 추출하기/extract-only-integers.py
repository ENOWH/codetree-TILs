A, B = input().split()
str_A = ''
str_B = ''

for elem in A:
    if elem >= '0' and elem <= '9':
        str_A += elem
    else:
        break

for elem in B:
    if elem >= '0' and elem <= '9':
        str_B += elem
    else:
        break

print(int(str_A)+int(str_B))