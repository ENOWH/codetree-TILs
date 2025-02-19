class Point:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number

n = int(input())
points = []

for i in range(n):
    x, y = tuple(map(int, input().split()))
    points.append(Point(x, y, i+1))

points.sort(key = lambda point: abs(point.x)+abs(point.y))

for point in points:
    print(point.number)