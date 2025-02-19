# 입력 처리
n = int(input())  # 수열의 길이
arr = list(map(int, input().split()))  # 수열 입력

# 각 숫자와 원래 인덱스를 저장
indexed_arr = [(val, idx) for idx, val in enumerate(arr)]

# 값 기준 정렬 (값이 같으면 원래 순서 유지)
indexed_arr.sort()

# 정렬된 위치를 저장할 리스트
position = [0] * n

# 정렬 후 각 숫자가 새로운 배열에서 어느 위치로 이동했는지 저장
for new_idx, (_, original_idx) in enumerate(indexed_arr):
    position[original_idx] = new_idx + 1  # 1-based index로 출력

# 결과 출력
print(" ".join(map(str, position)))