class Person:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

n = int(input())
persons = []

for _ in range(n):
    name, height, weight = tuple(input().split())
    persons.append(Person(name, int(height), int(weight)))

persons.sort(key = lambda x: (x.height, -x.weight))

for person in persons:
    print(person.name, person.height, person.weight)