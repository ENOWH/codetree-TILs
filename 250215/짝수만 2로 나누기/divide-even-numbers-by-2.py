n = int(input())
_list = list(map(int, input().split()))

def even(__list):
    for i in range(len(__list)):
        if __list[i]%2 == 0:
            __list[i] //= 2

even(_list)

for elem in _list:
    print(elem, end = " ")