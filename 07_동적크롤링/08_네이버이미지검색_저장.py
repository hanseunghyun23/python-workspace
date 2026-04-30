from playwright.sync_api import  sync_playwright
import requests #이미지 다운로드용
import os       #이미지 폴더 만들기 용
import  time    #잠시 대기하며 다음 검색을 위한 모듈
#from tests.demo_without_stealth_test import browser, page

def 단일검색():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    #이미지 저장할 폴더 만들기
    os.makedirs("다운로드이미지",exist_ok=True)#폴더가 있으면 스킵 없으면 자동생성
    #GetMapping("search.naver")
    #public String searchPage(@RequestParam String Where, @RequestParam String query = "고양이"){}
    page.goto(f"https://search.naver.com/search.naver?&where=image&query=고양이")
    time.sleep(2)


    #고양이 이미지 데이터 가져오기
    이미지목록 = page.locator("._fe_image_tab_content_thumbnail_image").all()
    print(f"=== 고양이 : {len(이미지목록)} 개 발견")

   # for 번호,이미지한장씩 in enumerate(이미지목록):
   # for 번호,이미지한장씩 in enumerate(이미지목록, start1):
    for 번호,이미지한장씩 in enumerate(이미지목록[:5]):
        이미지주소 = 이미지한장씩.get_attribute("src")  # 이미지 태그에서 속성 데이터 가져오기. src= 이미지경로 alt = "이미지 없을 때 보여질 별칭 스크린리더"

        if not 이미지주소:
            continue

        try:
            #이미지가있다 시작하자 저장을
            응답 = requests.get(이미지주소, timeout=5)

            #파일로 저장
            # f"문자열"은 print 상관 없이 문자열을 작성하는 어디든지 변수+글자를 섞어 작성할 때 어디서든 사용 가능
            파일이름 = f"다운로드이미지/고양이_{번호+1}.jpg"
            f=open(파일이름,"wb") #wb = 바이너리 쓰기모드
            f.write(응답.content)
            f.close()
            print(f"저장완료 : {파일이름}")
        except:
            print(f"{번호+1}번 이미지 저장 실패")
    time.sleep(2)
    browser.close()
    p.stop()
    print("폴더 이미지 저장 완료")


단일검색()



