# requests 라이브러리 불러오기
# → 파이썬으로 웹 서버에 HTTP 요청을 보내기 위한 도구
import requests

# jsonplaceholder는 연습용(가짜) API 서버
url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
todos = response.json()

not_completed = [
    todo                    # 조건을 만족하면 이 값을 새 리스트에 추가
    for todo in todos        # todos 리스트에서 todo 하나씩 꺼내서
    if not todo["completed"] # completed == False 인 경우만 선택
]

print("완료되지 않은 TODO 개수:", len(not_completed))
print("\n[완료되지 않은 TODO 5개만 출력]")

for todo in not_completed[:5]:
    # todo는 하나의 할 일(dict)
    # todo['id']     → 할 일 번호
    # todo['title']  → 할 일 제목
    print(f"- (id={todo['id']}) {todo['title']}")


# print(type(response), "response type")
# print(type(todos), "todos type")
# print(type(not_completed), "not_completed type")
# print(type(todo), "todo type")