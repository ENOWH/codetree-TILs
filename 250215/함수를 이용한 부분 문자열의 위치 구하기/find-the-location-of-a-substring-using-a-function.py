text = input()
pattern = input()

def index(s1, s2):
    index=-1
    for i in range(len(s1)-len(s2)+1):
        if s1[i:i+len(s2)] == s2:
            index = i
            break
    return index

print(index(text, pattern))