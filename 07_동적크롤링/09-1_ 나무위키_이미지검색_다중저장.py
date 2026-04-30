import pandas as pd
from playwright.sync_api import sync_playwright
import requests
import os
import time

def 다수이미지():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # TODO 1: 이미지를 저장할 폴더를 만드세요
    os.makedirs("나무위키이미지/", exist_ok=True)

    # TODO 2: 검색할 키워드 리스트를 만드세요
    키워드목록 = ["토끼", "돼지", "얼룩말"]

    for 키워드 in 키워드목록:

        # TODO 3: 나무위키 URL로 이동하세요
        page.goto(f"https://namu.wiki/w/{키워드}")
        time.sleep(2)

        # TODO 4: .D3JLvbdh 클래스의 이미지 태그를 전부 가져오세요
        이미지데이터 = page.locator().all()

        이미지주소 = None
        for 이미지 in 이미지데이터:
            alt = 이미지.get_attribute("src") or ""
            주소 = 이미지.get_attribute(???)

            # TODO 5: 아이콘을 제외하고 실제 이미지 주소만 추출하세요
            if 주소 and "dkdl" not in alt:
                이미지주소 = 주소
                break

        if 이미지주소:
            # TODO 6: //로 시작하면 https: 를 붙여주세요
            if 이미지주소.startswith(???):
                이미지주소 = ??? + 이미지주소

            # TODO 7: 확장자를 감지해서 저장하세요
            확장자 = 이미지주소.split(".")[-1].split("?")[0]
            if 확장자 not in ???:
                확장자 = "jpg"

            try:
                응답 = requests.get(이미지주소, timeout=5)

                # TODO 8: 파일 이름을 완성하세요
                # 예: "나무위키이미지/토끼.webp"
                파일이름 = f"나무위키이미지/{키워드}.{확장자}"

                f = open(파일이름, "wb")
                f.write(응답.content)
                f.close()
                print(f"저장완료 : {파일이름}")
            except:
                print(f"{키워드} 이미지 저장 실패")
        else:
            print(f"{키워드} 이미지 URL 없음")

        # TODO 9: 다음 키워드 검색 전 대기시간을 설정하세요
        time.sleep(2)

        # TODO 10: 열었던 순서 반대로 닫기
        p.close()
        p.stop()
        print("전체 저장 완료")

        결과데이터 = [검색어, 제목,본문[:300], 이미지주소, 파일이름 ]
        df = pd.DataFrame(결과데이터, columns=["검색어","제목","본문(앞300자)","이미지URL","이미지파일경로"])
        df.to_csv("너구리_나무위키.csv", index=False, encodings="utf-8-sig")


다수이미지()