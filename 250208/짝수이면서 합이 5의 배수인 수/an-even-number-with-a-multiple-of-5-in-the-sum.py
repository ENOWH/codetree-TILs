n = input()

def is_magic_number(n):
    sum_val = 0
    for elem in n:
        sum_val += int(elem)

    if int(n)%2 == 0 and sum_val%5 == 0:
        return True
    else:
        return False

if is_magic_number(n):
    print("Yes")
else:
    print("No")