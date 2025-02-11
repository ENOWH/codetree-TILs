n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def subsequence(a, b):
    num1 = len(a)
    num2 = len(b)

    for i in range(num1-num2+1):
        if a[i:i+num2] == b:
            return True
    
    return False

if subsequence(a, b):
    print("Yes")
else:
    print("No")