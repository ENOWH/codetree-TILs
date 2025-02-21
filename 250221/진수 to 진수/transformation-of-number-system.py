A, B = tuple(map(int, input().split()))
N = input()

def to_decimal(n, number):
    num = 0
    for i in range(len(n)):
        num = num*number + int(n[i])
    return num

def to_number(n, number):
    digits = []
    while True:
        if n<number:
            digits.append(n)
            break
        digits.append(n%number)
        n //= number
    return int("".join(map(str, digits[::-1])))

result = to_decimal(N, A)
result = to_number(result, B)
print(result)