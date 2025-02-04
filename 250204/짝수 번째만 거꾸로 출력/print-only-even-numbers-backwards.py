string = input()
reverse_string = []

for i in range(len(string)-1, -1, -1):
    if i%2!=0:
        reverse_string.append(string[i])

for elem in reverse_string:
    print(elem, end = "")