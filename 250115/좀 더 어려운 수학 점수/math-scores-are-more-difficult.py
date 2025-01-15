inp_A = input()
inp_B = input()
arr_A = inp_A.split()
arr_B = inp_B.split()
math_A, eng_A = int(arr_A[0]), int(arr_A[1])
math_B, eng_B = int(arr_B[0]), int(arr_B[1])

if math_A > math_B or (math_A==math_B and eng_A>eng_B):
    print("A")
else:   
     print("B")