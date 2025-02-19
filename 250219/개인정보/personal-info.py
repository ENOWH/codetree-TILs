class Person:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

persons = []

for _ in range(5):
    name, height, weight = tuple(input().split())
    persons.append(Person(name, int(height), float(weight)))

persons.sort(key = lambda x : x.name)

print("name")
for person in persons:
    print(person.name, person.height, person.weight)

persons.sort(key = lambda x : -x.height)
print()
print("height")
for person in persons:
    print(person.name, person.height, person.weight)