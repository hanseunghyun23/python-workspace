#방법1번
import newspaper
from newspaper import Article
import nltk
import requests
from bs4 import  BeautifulSoup

nltk.download('punkt_tab')

def news1():


    # 기계가 아니라 사람이 브라우저 접근한 척
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }


    주소 = "https://n.news.naver.com/article/277/0005755604?ntype=RANKING"
    웹사이트_응답 = requests.get(주소, headers=headers)
    soup = BeautifulSoup(웹사이트_응답.text, "html.parser")

    # 제목
    title = soup.find("h2", class_="title_area")
    print("제목 : ", title.strip() if title else "못찾음")

    # 본문
    content = soup.find("article", class_="dic_area")
    print("내용 : ", content.text.strip() if content else "못찾음")

    # 기자 이름 & 이메일
    reporter = soup.find("span", class_="byline_s")
    print("기자 : ", reporter.text if reporter else "못찾음")

news1()

def news2():
    주소 = "https://n.news.naver.com/article/277/0005755604?ntype=RANKING"

    article = newspaper.article(주소, language="ko")
    # article.download() nltk 안에 있는 punkt_tab가져와서 설치하기를 최초1회 실행하고 나면 매번 작성할 필요 X
    article.parse()

    print("제목 : " , article.title)
    print("내용 : " , article.text)
    print("기자 : " , article.authors)
    print("날짜 : " , article.publish_date)

news2()
