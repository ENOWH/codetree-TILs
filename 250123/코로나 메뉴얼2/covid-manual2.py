cnt_A, cnt_B, cnt_C, cnt_D = 0,0,0,0
for _ in range(3):
    symptom, temp = input().split()
    temp = int(temp)
    if symptom=='Y' and temp>=37:
        cnt_A+=1
    elif symptom=='N' and temp>=37:
        cnt_B+=1
    elif symptom=='Y' and temp<37:
        cnt_C+=1
    else:
        cnt_D+=1

print(cnt_A, cnt_B, cnt_C, cnt_D, end = " ")
if cnt_A>=2:
    print("E")