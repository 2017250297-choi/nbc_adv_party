# 파일 입출력
* open: 열기. 경로 + 모드(r: 읽기, w: 쓰기 ...)
* close: 닫기. 열었으면 반드시 닫는다.
## 운영체제별 경로 차이
window: C:\
POSIX : /

```python
# 파일을 쓰기 모드로 엽니다.
file = open("example.txt", "w")

# 파일에 데이터를 작성합니다.
file.write("Hello, world!\n")
file.write("This is an example file.\n")
file.write("Writing some lines.\n")

# 파일을 닫습니다.
file.close()

# 파일을 읽기 모드로 열고 데이터를 읽는 예제입니다.
file = open("example.txt", "r")

# 파일 전체를 읽어옵니다.
contents = file.read()
print("전체 내용:")
print(contents)

# 파일을 닫습니다.
file.close()

# 파일을 다시 읽기 모드로 열고 한 줄씩 읽는 예제입니다.
file = open("example.txt", "r")

print("한 줄씩 읽기:")
# 파일의 각 줄을 반복하며 읽어옵니다.
for line in file:
print(line.strip())

# 파일을 닫습니다.
file.close()

# 파일을 읽기 모드로 열고 모든 줄을 읽어 리스트로 반환하는 예제입니다.
file = open("example.txt", "r")

lines = file.readlines()
print("리스트로 읽기:")
print(lines)

# 파일을 닫습니다.
file.close()
```

# Json 다루기 - load, loads, dump, dumps
## 1. loads: JSON 문자열을 python 객체로 변환
```python
import json

# JSON 문자열
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# JSON 문자열을 Python 객체로 변환
data = json.loads(json_data)

# Python 객체 출력
print(data)
print(type(data))
```
## 2. load: JSON 파일을 python 객체로 변환

## 3. dumps/dump: python 객체를 JSON문자열/JSON파일로 변환

https://jsonplaceholder.typicode.com/posts


# Request 모듈 다루기
1. get 요청 보내기
```python
import requests

response=requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.text)
```
2. post 요청 보내기
```python
import requests

data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=data)
print(response.text)
```
3. put, delete 보내기


# CURL 사용
postman 대신 cli 환경에서 테스팅이 가능하다.
```bash
curl https://jsonplaceholder.typicode.com/posts #get
curl -X POST -d"title=foo&body=bar&usrId=1" https://jsonplaceholder.typicode.com/posts #post
curl -X PUT -d"title=foo&body=bar&usrId=1" https://jsonplaceholder.typicode.com/posts/1 # put
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1 # delete
```
내 장고 프로젝트에 직접 테스트 해보자.

# CSV 파일 다루기
AI, 데이터 분석을 위한 대용량 빅 데이터를 표현하는데 주로 사용된다. (백엔드에서 주로 다루지는 않는다.)
