from playwright.sync_api import sync_playwright
import requests  # 이미지 다운로드 용
import os        # 이미지 폴더 만들기 용
import time

from tests.demo_persistent_test import browser

p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
page = browser.new_page()
os.makedirs("나무위키이미지",exist_ok=True)
page.goto("https://namu.wiki/w/늑대")
time.sleep(2)

이미지데이터 = page.locator("이미지 데이터 클래스 명칭").all()
if 이미지데이터:
    이미지주소 = 이미지데이터[0].get_attribute("src") # 이미지는 보통 다수 존재한다가 기본! 한장인 경우에도 이미지[0] = 맨 앞에있는 데이터 가져온다 표기

    if 이미지주소:
        if 이미지주소.startswith("//"):
            이미지주소 = "https" + 이미지주소
        try:
            응답 = requests.get(이미지주소, timeout=5)
            파일이름 = "나무위키이미지/늑대.jpg"
            f= open(파일이름,"wb")
            f.close()
            print(f"저장완료 : {파일이름}")
        except:
            print("이미지 저장 실패")
    else:
        print("이미지 URL 없음")

browser.close()

