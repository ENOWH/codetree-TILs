inp = input()
arr = inp.split()
a, b = int(arr[0]), int(arr[1])

i = a
while i <= b:
    if i%2==0:
        print(i, end = " ")
    i += 1