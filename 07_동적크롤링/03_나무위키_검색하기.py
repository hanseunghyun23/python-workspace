from playwright.sync_api import  sync_playwright
import time

def 나무위키기본():
    p = sync_playwright().start()       #playwright 실행 시작
    browser = p.chromium.launch(headless=False) #크롬 브라우저 열기 headless=False 검색하는 창 보이기 True 하면 검색하는 화면 안보임
    page = browser.new_page()

    검색어목록=["강아지","고양이","토끼"] # 검색할 단어 리스트

    for 검색 in 검색어목록:    #나무위키 해당 단어 페이지로 이동
        page.goto(f"https://namu.wiki/w/{검색}")
        time.sleep(2) # 패아지 로딩 기다리기 2초

        제목=page.title() # 브라우저 탭 제목 가져오기

        본문 = page.locator("body").inner_text() #body 태그 안의 전체 텍스트 가져오기

        print(f"=== {검색}")      #현재 검색어 출력
        print(f"제목 : {제목}")    #제목 출력
        print(f"본문 앞부분 {본문[:300]}") #본문 앞 300글자만 출력
        print()

        time.sleep(2) #다음 검색 전 2초 대기 너무 빨리 검색하면 봇인걸 인지하고 차단될 수 있음

    browser.close()
    p.stop()
