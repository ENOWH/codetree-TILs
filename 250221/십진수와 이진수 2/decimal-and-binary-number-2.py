N = input()

def to_decimal(n):
    num = 0
    for i in range(len(n)):
        num = num*2 + int(n[i])
    return num

def to_binary(n):
    digits = []
    while True:
        if n<2:
            digits.append(n)
            break
        digits.append(n%2)
        n //= 2
    return "".join(map(str, digits[::-1]))

result = to_decimal(N)*17
result = to_binary(result)
print(result)