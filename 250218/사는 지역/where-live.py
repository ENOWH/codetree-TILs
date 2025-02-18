class Person:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region

n = int(input())
persons = []

for _ in range(n):
    name, address, region = tuple(input().split())
    persons.append(Person(name, address, region))

slowest_idx = 0
for i in range(1, n):
    if persons[slowest_idx].name < persons[i].name:
        slowest_idx = i

print(f"name {persons[slowest_idx].name}")
print(f"addr {persons[slowest_idx].address}")
print(f"city {persons[slowest_idx].region}")