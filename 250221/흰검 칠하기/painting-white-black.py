n = int(input())  # 명령 개수
commands = [input().split() for _ in range(n)]  # 명령 리스트

position = 0  # 현재 위치
tiles = {}  # {위치: 칠해진 횟수}

for command in commands:
    distance, direction = int(command[0]), command[1]
    
    if direction == 'L':
        for i in range(position, position - distance, -1):  # 왼쪽으로 이동
            tiles[i] = tiles.get(i, 0) + 1
        position -= (distance - 1)  # 마지막 위치 반영

    elif direction == 'R':
        for i in range(position, position + distance):  # 오른쪽으로 이동
            tiles[i] = tiles.get(i, 0) + 1
        position += (distance - 1)  # 마지막 위치 반영

# 색상 개수 카운트
white, black, gray = 0, 0, 0

for count in tiles.values():
    if count >= 2:
        gray += 1
    elif count == 1:
        black += 1  # 마지막에 칠해진 색이 검은색('R')이므로 기본값이 검은색

print(white, black, gray)