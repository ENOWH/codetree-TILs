secret_code, meeting_point, time = input().split()
time = int(time)

class program:
    def __init__(self, s, m, t):
        self.secret_code = s
        self.meeting_point = m
        self.time = t

program1 = program(secret_code, meeting_point, time)
print("secret code :", program1.secret_code)
print("meeting point :", program1.meeting_point)
print("time :", program1.time)