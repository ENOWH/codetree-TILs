def find_max(arr):
    # 기저 조건: 리스트에 원소가 하나만 남으면 그 값이 최댓값
    if len(arr) == 1:
        return arr[0]
    
    # 첫 번째 원소와 나머지 원소 중 최댓값 비교
    return max(arr[0], find_max(arr[1:]))

# 입력 처리
n = int(input())  # 원소 개수
arr = list(map(int, input().split()))  # 리스트 입력

# 최댓값 출력
print(find_max(arr))