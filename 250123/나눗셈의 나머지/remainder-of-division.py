# 입력 받기
a, b = map(int, input().split())

# 나머지 등장 횟수를 저장할 배열
arr = [0] * b

# 나눗셈 반복
while a > 0:
    remainder = a % b  # 현재 나머지 계산
    arr[remainder] += 1  # 나머지 횟수 기록
    a //= b  # a를 b로 나눔

# 각 나머지의 횟수 제곱의 합 계산
sum_val = sum(x ** 2 for x in arr)

# 결과 출력
print(sum_val)