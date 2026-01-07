import requests

url = "https://jsonplaceholder.typicode.com/posts"

# 쿼리 파라미터(query parameter)
# userId=1 인 게시글만 달라고 서버에 요청하기 위한 조건
# 브라우저 주소로 치면 ?userId=1 과 같은 의미
params = {"userId": 1}

# params=params params 변수 선언한걸 앞의 params 에 넣는다.
response = requests.get(url, params=params)

# 파싱
posts = response.json()

print("=== 'qui'가 포함된 제목 목록 ===")


# posts 리스트에 들어 있는 게시글을 하나씩 꺼내서 반복
for post in posts:
    # post는 하나의 게시글이며, 딕셔너리(dict) 형태
    # post["title"] 은 게시글의 제목
    # "qui" in post["title"] 은
    # 제목 안에 'qui'라는 문자열이 포함되어 있는지 확인
    if "qui" in post["title"]:
        # 조건을 만족하는 경우에만 출력
        # post['id']    → 게시글 번호
        # post['title'] → 게시글 제목
        print(f"[id={post['id']}] {post['title']}")