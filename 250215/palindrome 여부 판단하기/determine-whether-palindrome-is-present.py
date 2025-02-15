string = input()

def palindrome(str_):
    str_1 = str_[::-1]
    if str_1 == str_:
        print("Yes")
    else:
        print("No")

palindrome(string)