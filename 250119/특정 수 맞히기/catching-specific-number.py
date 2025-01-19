while True:
    # 변수 선언 및 입력
	n = int(input())
		
	# n이 25보다 작으면 Higher을, 25보다 크면 Lower을, 25와 같으면 Good을 출력한 뒤 종료합니다.
	if n < 25:
		print("Higher")
		
	elif n > 25:
		print("Lower")
		
	else:
		print("Good")
		break
