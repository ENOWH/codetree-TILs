word1 = input()
word2 = input()

def equal(a, b):
    for elem1, elem2 in zip(a, b):
        if elem1 != elem2:
            return False
    return True

if equal(word1, word2):
    print("Yes")
else:
    print("No")
