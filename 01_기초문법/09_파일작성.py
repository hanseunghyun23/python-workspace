'''
open("파일이름.확장자이름","모드",encoding="utf-8")
-파일이름.확장자이름이 존재하면 열어서 작업하는 것
-파일이름.확장자이름이 존재하지 안혹 작성모드일 경우 알아서 파일을 만들고 작성

open("파일명.txt", "w") write - 기존 내용 삭제하고 다시 새롭게 작성하기
open("파일명.txt", "r") read - 읽기모드
open("파일명.txt", "a") append - 기존 내용이 존재한다면 유지한 채 이어 쓰기


'''

파일 = open("my_diary.txt","w",encoding="utf-8")

while True:
    글자작성 = input("입력하세요 (그만하려면 q 입력):")
#만약 Q 를 작성해도 작성종료로 하고 싶다면
#upper() = 대문자로 통일
#lower() = 소문자로 통일
# 위 둘중 하나를 이용해서 대문자 Q를 작성해도 종료하게끔 처리

    if 글자작성.lower() =="q":
        print("저장완료")
        break

    파일.write(글자작성 + "\n")
파일.close()