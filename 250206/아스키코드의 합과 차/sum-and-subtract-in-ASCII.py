first, second = input().split()

first = ord(first)
second = ord(second)

sum_val = first + second

if first >= second:
    diff_val = first-second
else:
    diff_val = second-first

print(sum_val, diff_val)