A = input()

def judge(s):
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            return True
    return False

if judge(A):
    print("Yes")
else:
    print("No")