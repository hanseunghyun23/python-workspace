'''
밤범 2가지
1 : request + BeautifulSoup

2: newspaper3k 뉴스수집 전용 라이브러리로 수집하는 방법
pip install newspaper3k
'''

import requests
from bs4 import BeautifulSoup

def 방법1번():
    주소 = "https://v.daum.net/v/20260428091147574"

        # 기계가 아니라 사람이 브라우저 접근한 척
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }

    웹사이트_응답 = requests.get( 주소 , headers=headers)
    soup = BeautifulSoup(웹사이트_응답.text, "html.parser")
#soup = request로 가져온 텍스트를 분해했고, 분해한 데이터가 들어있는 공간
#제목
#분해한 공간에서 하나의 데이터 찾기

#제목
    title = soup.find("h3", class_="tit_view")
    print("제목 : " , title.text if title else "못찾음")

#내용
    content = soup.find("div", class_="article_view")
    print("내용 : " , content.text if content else "못찾음")

    reporter = soup.find("span", class_="reporter_view")
    print("내용 : " , reporter.text if reporter else "못찾음")

방법1번()

'''
newpaper3k 는 업데이트 중단됨
pip install newspaper4k lxml_lxml_clean
'''

import newspaper
from newspaper import Article
import nltk
nltk.download('punkt_tab')

def newspaper3k_Old_Version():
    주소 = "https://v.daum.net/v/20260428091147574"

    article = newspaper.article(주소, language="ko")
   # article.download()
    article.parse()

    print("제목 : " , article.title)
    print("내용 : " , article.text)
    print("기자 : " , article.authors)
    print("제목 : " , article.title)
def newspaper4_New_Version():
    주소 = "https://v.daum.net/v/20260428091147574"

    article = newspaper.article(주소, language="ko")
# article.download()
    article.parse()

    print("제목 : " , article.title)
    print("내용 : " , article.text)
    print("기자 : " , article.authors)
    print("제목 : " , article.title)

newspaper4_New_Version()