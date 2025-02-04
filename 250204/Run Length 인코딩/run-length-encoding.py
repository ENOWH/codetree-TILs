A = input()
length = len(A)

curr_char = A[0]
prev_char = A[0]

num_char = 1
encoded = ""

for i in range(1, length):
    curr_char = A[i]
    if curr_char == prev_char:
        num_char += 1
    else:
        encoded += prev_char
        encoded += str(num_char)

        num_char = 1
        prev_char = curr_char

encoded += prev_char
encoded += str(num_char)

print(len(encoded))
print(encoded)