'''
os(Operating System)
-운영체제와 상호작용하는 파이썬 기본 내장 모듈
- 파일 / 폴더 관련 작업을 코드로 가능하게 해줌
pip install 없이 바로 사용 가능
'''
import os

def 폴더작업():
    #폴더생성
    os.makedirs("새폴더")
    os.makedirs()

    print(os.getcwd())

    #작업 경로 변경 ->실행할 때 제대로 컴퓨터 구조를 알지 못하면 골치이픈 상황 발생
    os.chdir("C:/Users/AdminH/OneDrive/desktop")

    print(os.listdir("."))
    print(os.listdir("C:/Users/AdminH/OneDrive/바탕화면"))


def 파일작업():
    #파일 폴더 존재여부 확인
    os.path.exists("파일이름.확장자") # 결과는 Boolean True / False 나온다


    os.path.isfile("파일이름.확장자") #파일이면 결과는 True
    os.path.isdir("폴더이름")         #파일이면 결과는 True

    # 파일삭제
    os.remove("파일이름.확장자")

    #파일이름만 갖고오기
    os.path.basename("폴더1번/폴더2번/폴더3번/파일이름.확장자") #파일이름.확장자

    #파일이름과 확장자 분리
    os.path.splitext("파일이름.확장자") # ("파일이름", ".csv")

    os.path.join("폴더1번/폴더2번/폴더3번","파일이름.확장자")
