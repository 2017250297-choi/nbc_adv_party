def my_coroutine():
    while True:
        value = yield
        print("Received value:", value)


# 코루틴 객체 생성
co = my_coroutine()

# 코루틴 실행 준비
next(co)
next(co)
# 값을 보내기
co.send("Hello, world!")
co.send("Hello, world!")
co.send("Hello, world!")


def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3


def my_coroutine():
    while True:
        x = yield
        print("Received:", x)


co = my_coroutine()
next(co)

co.send(10)  # Received: 10
co.send(20)  # Received: 20
co.send(30)  # Received: 30

phone_book = {"a": "123-4567", "b": "234-5678", "c": "456-7890"}


def search():
    name = yield
    while True:
        if name in phone_book:
            phone_no = phone_book[name]
        else:
            phone_no = "Can not find"
        name = yield phone_no


search_coroutine = search()
next(search_coroutine)
ret = search_coroutine.send("a")
print(ret)  # 123-4567
ret = search_coroutine.send("b")
print(ret)  # 234-5678
ret = search_coroutine.send("c")
print(ret)  # 456-7890

import asyncio
import random


async def fetch_data():
    print("데이터를 가져오는 중...")
    await asyncio.sleep(1)  # 데이터를 가져오는데 1초가 걸린다고 가정
    return random.randint(1, 100)


# 너무 오래걸리는 작업이라 병렬적으로 실행될 필요는 있지만
# 결국 코루틴의 결과가 필요하다.
async def main():
    data = await fetch_data()
    print(f"가져온 데이터: {data}")


asyncio.run(main())
