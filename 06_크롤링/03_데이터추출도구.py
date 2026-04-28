'''
BeautifulSoup
- request로 받아온 HTML 을 분석(파싱)해서 원하는 데이터를 뽑아주는 도구

Soup = 뒤죽박죽 엉킨 HTML 코드
Beautiful = 예쁘게 정리하서 개발자가 원하는 소스만 가져오겠다

pip install beautifulsoup4
'''
from bs4 import BeautifulSoup

html ='<h2 id = "title">오늘의 뉴스</h2><p class="content">내용</p>'

soup = BeautifulSoup(html, "html.parser")

#태그로 찾기
print(soup.find("h2").text)

#id로 찾기
print(soup.find(id="title").text)

#class로 찾기
print(soup.find(class_="content").text)

items = soup.find_all("p")




