from playwright.sync_api import  sync_playwright
import time

p = sync_playwright().start() #크롤링을 시작하지
웹사이트 = p.chromium.launch(headless=False) #크롬을 이용해서 검색 시작하겠다. head는 없다
page= 웹사이트.new_page() #웹사이트 새 페이지 띄우기 기능
#검색어 리스트로 강아지 고양이 토끼 넣고 for문을 이용해 강아지, 고양이, 토끼 검색하기

검색어목록=["강아지","고양이","토끼"]
for i in 검색어목록:
    page.goto(f"https://search.naver.com/search.naver?query={i}")
    print(page.title()) #2초 대기후 다음 검색
    time.sleep(2)       #웹사이트 창 닫기

웹사이트.close()    #크롤링 종료
p.stop()


