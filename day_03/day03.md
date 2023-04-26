# 1. 재귀의 이해
> 재귀함수: 스스로를 호출하는 함수이다.

주요한 이유: 재귀함수를 모르면 못푸는 문제 유형: DFS, BFS, 트리순회(traversal)

```python
def rec(n):
    if n ==0:
        return 0
    else:
        return n + rec(n-1)

print(rec(4))  # 4+3+2+1+0 = 10

def rec2(n):
    if n<5:
        print(n)
        rec2(n+1)
rec2(1) # 1 2 3 4
```

유의사항 1: 모든 재귀함수는 반복문으로 치환 가능하다.
유의사항 2: 재귀함수에는 반드시 종료조건이 있어야한다. 종료조건이 없으면 무한히 재귀호출하므로, 이를 막기 위해 오류가 발생한다.
```python
RecursionError: maximum recursion depth exceeded while calling a Python object
```
print(sys.getrecursionlimit()) 을 통해 현재 정해진 최대 재귀 깊이 (maximum recursion depth)를 알 수 있다.

## 재귀로 접근해야하는 문제 알아채는법
> **문제푸는 전체과정을 볼때, 일부분을 푸는 과정이 전체를 푸는 과정과 유사할 경우**

예시:
1 부터 n까지의 자연수 총합 구하기, 팩토리얼 구하기, 피보나치
> n! = n * (n-1)!
```python
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
```
> fib[n] = fib[n-1]+fib[n-2], fib[1]=0, fib[2]=1
```python
def fib(n):
    if 2 >= n:
        return n-1
    return fib(n-1)+fib(n-2)
```

# 2. 클래스 심화
## 0. 상속 되짚기
Animal -> cat, dog

## 1. 메서드 오버라이딩
서브 클래스에서 **상위클래스의 메서드를 재정의** 하는 것을 의미한다. **이름은 같지만 다른 기능을 수행하고 싶을 때, 기능추가/수정 하고싶을 때** 사용한다.

### django에서의 오버라이딩
1. 모델 클래스: save()를 오버라이딩해 저장전 에 특정 작업 수행
2. 폼 클래스: clean()을 재정의해 유효성검사 리폼가능
3. 뷰 클래스: dispatch()를 오버라이딩해...

**즉 내장 메서드 쓰고는 싶은데 좀 바꾸고 싶을 때 쓰면 좋다**

## 2. 추상 클래스
자체적으로 **객체를 생성하지 않고** 상속받는 **하위클래스에서 반드시 구현해야하는 추상 메서드**를 가지고 있다. 즉 **인터페이스/형태만 정의**되어있다.

### 장고에서의 사용
BaseModel: 추상클래스


# 차주예고
다형성과 데코레이터(DRF에서 매우 중요!)