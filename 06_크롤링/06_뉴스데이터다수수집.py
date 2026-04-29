#방법1번
import newspaper
from newspaper import Article
import nltk
import requests
from bs4 import  BeautifulSoup
import time
nltk.download('punkt_tab')
'''
select vs find
soup.select()
- CSS 선택자
- 리스트(여러개)
- 동일한 태그 동일한 id 나 class 로 다수 데이터를 가져올 때 사용
- css style에 작성하는 것 처럼 .클래스이름 #아이디이름 표기

soup.find_all("태그이름", class_="클래스이름" id="아이디이름")
- select와 완전 동일
- css 선택자 스타일 작성이 어려움;
- 위와 같이 "태그이름" , class or id 명칭으로 다수 데이터를 가져올 때 사용

soup.find()
- 하나의 데이터를 가져올 때 사용
- 태그 + 속성 직접 지정

.startwith("/")
- ~ 로 시작하는지 확인하는 기능
- "안녕하세요".startwith("안녕") 안녕하세요는 안녕으로 시작하는게 맞으므로 True
- "안녕하세요".startwith("hi") 안녕하세요는 hi로 시작하는 게 아니므로 False

크롤링을 할 때 웹사이트 링크는 두 종류로 나뉜다
#절대경로 - 주소가 완전히 다 있는 상태


#상대경로 - 앞부분이 생략됨

보통 상대경로는 앞이 https가 아니라 / 로  시작한다
'''
def news1():


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

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
}

#네이버 뉴스 랭킹 페이지에서 URL 20개 자동 수집
def url목록가져오기():
    랭킹주소="https://news.naver.com/main/ranking/popularDay.naver"
    res = requests.get(랭킹주소,headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    랭크목록=[]
    태그들 = soup.select("a.list_title")


    for 태그 in 태그들[:20]:
        링크 = 태그.get("href")
        if 링크 and "article" in 링크:
            if 링크.startswith("/"):
                링크 = "https://news.naver.com" + 링크
            랭크목록.append(링크)
    print(f"총{len(랭크목록)} 개 URL 수집 완료")
    return 랭크목록

def 기사수집(url):
    아티클= newspaper.article(url, language="ko")
    아티클.parse()

    res= requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    기자태그 = soup.find("span", class_="byline_s")
    날짜태그 = soup.find("span", class_ ="media_end_head_info_datestamp_time" )

    제목 = 아티클.title
    내용 = 아티클.text[:100] + "..."
    기자 = 기자태그.text.strip() if 기자태그 else "못찾음"
    날짜 = 날짜태그.text.strip() if 날짜태그 else "못찾음"

    return 제목,내용,기자,날짜


def 뉴스20개수집():
    url목록 = url목록가져오기()

    #순서번호
    for i, url in enumerate(url목록):
        print(f"\n{i+1}번째 뉴스기사")
        제목, 내용, 기자, 날짜 = 기사수집(url)
        print("제목 : ",제목)
        print("내용 : ",내용)
        print("기자 : ",기자)
        print("날짜 : ",날짜)
        time.sleep(1)

    print("수집 완료")
뉴스20개수집()




