inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

print((a+b+c), int((a+b+c)/3), int((a+b+c)-((a+b+c)/3)), sep = '\n')