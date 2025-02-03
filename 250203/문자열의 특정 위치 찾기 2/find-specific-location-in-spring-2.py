arr = ["apple", "banana", "grape", "blueberry", "orange"]
alphabet = input()
cnt=0

for i in range(5):
    if arr[i][2] == alphabet or arr[i][3] == alphabet:
        print(arr[i])
        cnt+=1
print(cnt)