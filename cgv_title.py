# import requests
# from bs4 import BeautifulSoup

# url ="https://quotes.toscrape.com/"
# resp = requests.get(url)
# resp.raise_for_status()
# soup = BeautifulSoup(resp.text,"lxml")

# # 첫 번째 명언 블록 선택
# quote = soup.select_one("div.quote")

# # 명언 내용과 저자 태그 선택
# text_tag = quote.select_one("span.text")
# author_tag = quote.select_one("small.author")

# print(type(text_tag)) <class 'bs4.element.Tag'>

# print("첫 번째 명언:")
# print("내용:", text_tag.text.strip())
# print("저자:", author_tag.text.strip())

# #select_one 첫번째 1개만 들고오는 메서드

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
resp = requests.get(url)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "lxml")

quotes = soup.select("div.quote")

print("📝 현재 페이지 명언 목록")
print("=" * 40)



for i, quote in enumerate(quotes, start=1):
    text_tag = quote.select_one("span.text")
    author_tag = quote.select_one("small.author")

    if text_tag and author_tag:
        text = text_tag.text.strip()
        author = author_tag.text.strip()
        print(f"{i}. {text}  - {author}")