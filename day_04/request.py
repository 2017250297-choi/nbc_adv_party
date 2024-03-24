import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.text)

data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
print(response.text)

data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", data=data)
print(response.status_code)

response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
