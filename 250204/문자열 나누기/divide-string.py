n = int(input())
arr = list(input().split())
tot_str = ""

for i in range(n):
    tot_str += arr[i]

for i in range(len(tot_str)):
    if i%5!=0 or i==0:
        print(tot_str[i], end = "")
    else:
        print()
        print(tot_str[i], end = "")
