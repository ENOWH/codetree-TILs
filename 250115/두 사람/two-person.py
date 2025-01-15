inp_A = input()
arr_A = inp_A.split()
age_A, sex_A = int(arr_A[0]), arr_A[1]

inp_B = input()
arr_B = inp_B.split()
age_B, sex_B = int(arr_B[0]), arr_B[1]

if (age_A>=19 and sex_A=='M') or (age_B>=19 and sex_B=='M'):
    print(1)
else:
    print(0)