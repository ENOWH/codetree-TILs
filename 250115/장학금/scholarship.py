inp = input()
arr = inp.split()
mid, final = int(arr[0]), int(arr[1])

if mid>=90 and final>=95:
    print("100000")
elif mid>=90 and final>=90:
    print("50000")
else:
    print("0")