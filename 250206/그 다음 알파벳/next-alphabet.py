alphabet = input()

if alphabet == 'z':
    alphabet = chr(ord('a')-1)
print(chr(ord(alphabet)+1))