#방법1번
import newspaper
from newspaper import Article
import nltk
import requests
from bs4 import  BeautifulSoup

nltk.download('punkt_tab')

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
