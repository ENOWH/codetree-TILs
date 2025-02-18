class Rainy:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
rainydays = [Rainy(date, day, weather) for date, day, weather in arr
if weather == 'Rain']

target_idx=0
for i, days in enumerate(rainydays):
    if days.date < rainydays[target_idx].date:
        target_idx = i

print(f"{rainydays[target_idx].date} {rainydays[target_idx].day} {rainydays[target_idx].weather}")