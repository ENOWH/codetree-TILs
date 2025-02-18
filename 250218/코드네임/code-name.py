MAX_N = 5

codenames = []
scores = []

class Agent:
    def __init__(self, c, s):
        self.codename = c
        self.score = s

for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

idx=0
for i in range(MAX_N):
    if scores[i] == min(scores):
        idx = i

print(codenames[idx], scores[idx])