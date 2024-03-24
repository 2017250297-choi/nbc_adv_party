import itertools

counts = itertools.count(5, 2)
for x in counts:
    if x > 20:
        break
    print(x, end=" ")

colors = ["r", "g", "b"]
cycle = itertools.cycle(colors)
for _ in range(6):
    print(next(cycle), end=" ")

# repeat - 정해진 값을 반복해서 반환

# chain - 덧셈같은 것

# permuations 순열, combinations 조합
# 파이선에서는 직접구현없이 그냥 이거 쓰면 된다.

# islice: 이터라블한 객체들을 슬라이싱 할 수 있다.
print()
##########################################
##########################################

"""
collections: 기능이 확장된 자료형들이 있다.
"""

import collections

# Counter: 요소안의 요소갯수 세기
fruit_count = collections.Counter([1, 2, 1, 2, 2, 3, 3, 3, 3, 3, 4])
print(fruit_count[1])
print(fruit_count.most_common(1))  # 가장흔한 요소와 갯수 확인

# DefaultDict

# Deque: 양방향큐


# 가변인자: 모듈을 직접 만들 때 유용하다.
def add(*args):
    ret = 0
    for i in args:
        ret += i
    return ret


print(add(1, 2, 3, 4, 5, 6, 7))
print(add(2, 3, 4))


def info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")


info(name="Adam", age=25, country="Korea")


def show_info(*args, **kwargs):
    print("positionals")
    for arg in args:
        print(arg, end=" ")
    print()
    print("kwords")
    for k, v in kwargs.items():
        print(f"{k} : {v}")


show_info(1, 2, 3, name="Adam", age=25, country="Korea")

# 람다함수
# 정렬(키값),필터링과 맵핑과 함께 자주 사용된다.

students = [
    {"name": "abc", "age": 10},
    {"name": "abd", "age": 3},
    {"name": "zzz", "age": 1},
]
students.sort(key=lambda student: student["age"])
print(students)
students.sort(key=lambda student: student["name"])
print(students)
