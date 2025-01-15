inp_A = input()
inp_B = input()
arr_A = inp_A.split()
arr_B = inp_B.split()
math_A, eng_A = int(arr_A[0]), int(arr_A[1])
math_B, eng_B = int(arr_B[0]), int(arr_B[1])

if math_A > math_B:
    print("A")
elif math_A < math_B:
    print("B")
else:
    if eng_A > eng_B:
        print("A")
    elif eng_A < eng_B:
        print("B")