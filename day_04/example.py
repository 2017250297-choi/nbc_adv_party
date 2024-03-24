import json

# with open("day_04/example.json", "r") as file:
#     data = json.load(file)
# print(data["employee"])

# # Python 객체
data = {"name": "John", "age": 30, "city": "New York"}

# Python 객체를 JSON 파일로 변환
with open("day_04/data2.json", "w") as file:
    json.dump(data, file)
