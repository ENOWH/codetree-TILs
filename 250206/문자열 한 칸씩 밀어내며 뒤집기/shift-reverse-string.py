input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

for i in range(q):
    if queries[i] == 1:
        input_str = input_str[1:] + input_str[0]
    elif queries[i] == 2:
        input_str = input_str[-1] + input_str[:-1]
    elif queries[i] == 3:
        arr = list(input_str)
        arr = arr[::-1]
        input_str = ''.join(arr)
    
    print(input_str)