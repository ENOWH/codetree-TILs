import sys

input_str = input()
target_str = input()

input_len, target_len = len(input_str), len(target_str)

for i in range(input_len):
    if i + target_len - 1 > input_len - 1:
        continue
    is_matched = True
    for j in range(target_len):
        if input_str[i+j] != target_str[j]:
            is_matched = False
        
    if is_matched:
        print(i)
        sys.exit(0)

print(-1)