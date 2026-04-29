'''
Selenium vs Playwright

Selenium
- 2004년 출시
- 가장 오래된 웹 자동화 도구
- 거의 모든 언어 지원
- 커뮤와 래퍼런스가 압도적으로 많음
- pip install selenium
- pip install webdriver-manger

Playwright
- 2020년 발표된 Microsoft가 만든 자동화 도구
- 비동기 처리가 기본
- 속도가 빠르고 현대적인 웹앱에 강함
- pip install playwright
- playwright install
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from tests.demo_without_stealth_test import browser
from webdriver_manager.chrome import ChromeDriverManager

def 셀레니움기본코드():
    #브라우저 열기
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #페이지 이동
    driver.get("https://google.com")

    #요소찾기 태그 안에 있는 데이터 찾기
    search_box = driver.find_element(By.NAME,"q")

    #텍스트 입력
    search_box.send_keys("셀레니움 이란")
    search_box.submit()

    #결과출력
    print(driver.title)

    #브라우저 닫기 = quit()
    driver.quit()

#셀레니움기본코드()

from playwright.sync_api import sync_playwright

#playwright 시작
def playwright기본코드():
    p = sync_playwright().start()

    #브라우저 열기
    browser = p.chromium.launch(headless=False,
                                args=["--disable-blink-features=AutomationControlled"])
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    )
    page = context.new_page()

    page.add_init_script("Object.defineProperty(vanigator,'webdriver,{get : () => undefined}")
    #새 페이지
    page = browser.new_page()

    #페이지 이동
    page.goto("https://google.com")

    #요소 찾고 입력
    page.fill('textarea[name="q"]', 'Playwright 란')
    page.keyboard.press("Enter")

    #결과 기다리기
    page.wait_for_load_state("networkidle")
    print(page.title())

    browser.close()
    p.stop()

# playwright기본코드()

#from playwright_stealth import stealth_sync 1버전대 사용법

#from playwright_stealth import Stealth
def playwrightSteal코드():
    p = sync_playwright().start()

    #브라우저 열기
    browser = p.chromium.launch(headless=False)
    #Stealth().use_sync(page).__enter__()

    #새 페이지
    page = browser.new_page()

    #페이지 이동
    page.goto("https://google.com")

    #요소 찾고 입력
    page.fill('textarea[name="q"]', 'Playwright 란')
    page.keyboard.press("Enter")

    #결과 기다리기
    page.wait_for_load_state("networkidle")
    print(page.title())

    browser.close()
    p.stop()











from playwright.sync_api import sync_playwright

def 구글대신네이버():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://search.naver.com/search.naver?query=강아지")

    browser.close()
    p.stop()
구글대신네이버()

