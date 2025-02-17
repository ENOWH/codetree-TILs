import math

# 두 수의 최소공배수(LCM) 계산
def lcm(a, b):
    return (a * b) // math.gcd(a, b)

# 리스트의 최소공배수를 재귀적으로 구하는 함수
def find_lcm(arr, n):
    if n == 1:
        return arr[0]  # 리스트에 하나만 남으면 그 값이 최소공배수

    return lcm(arr[n-1], find_lcm(arr, n-1))  # 마지막 값과 나머지 값들의 LCM 계산

# 입력 처리
n = int(input())
arr = list(map(int, input().split()))

# 최소공배수 출력
print(find_lcm(arr, n))