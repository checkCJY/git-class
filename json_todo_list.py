# requests 라이브러리 불러오기
# → 파이썬으로 웹 서버에 HTTP 요청(GET, POST 등)을 보내기 위한 도구
import requests

# 이 주소는 jsonplaceholder라는 "연습용 API 서버"
url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
print("Status Code:", response.status_code)
data = response.json()

print("응답 타입:", type(data))

print("전체 할 일 개수:", len(data))

first = data[0]
test = data

print("\n[첫 번째 TODO]")
print(first)
print("\n[앞 5개의 제목만 출력]")

for todo in data[:5]:
    # todo는 하나의 할 일(dict)
    # todo['id']     → 할 일 번호
    # todo['title']  → 할 일 제목
    print(f"- (id={todo['id']}) {todo['title']}")

