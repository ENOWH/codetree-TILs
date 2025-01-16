inp_1 = input()
arr_1 = inp_1.split()
symptom_1, temp_1 = arr_1[0], int(arr_1[1])

inp_2 = input()
arr_2 = inp_2.split()
symptom_2, temp_2 = arr_2[0], int(arr_2[1])

inp_3 = input()
arr_3 = inp_3.split()
symptom_3, temp_3 = arr_3[0], int(arr_3[1])

if (symptom_1=="Y" and temp_1>=37) and (symptom_2=="Y" and temp_2>=37):
    print("E")
elif (symptom_1=="Y" and temp_1>=37) and (symptom_3=="Y" and temp_3>=37):
    print("E")
elif (symptom_2=="Y" and temp_2>=37) and (symptom_3=="Y" and temp_3>=37):
    print("E")
else:
    print("N")