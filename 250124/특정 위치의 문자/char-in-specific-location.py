word = ['L', 'E', 'B', 'R', 'O', 'S']
idx=-1

n=input()

for i, char in enumerate(word):
    if char == n:
        idx = i

if idx==-1:
    print("None")
else:
    print(idx)
