alphabet = input()

if alphabet == 'a':
    alphabet = chr(ord('z')+1)

print(chr(ord(alphabet)-1))