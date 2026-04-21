'''
for - 끝이 정해져 있는 반복문
while - 끝이 정해져 있지 않은 반복문 에서 주로 사용

range() - 숫자 법위 만들기
몇 번 반복할지 숫자 범위를 만들어 주는 것

range() 구조
range(시작숫자, 끝나는 숫자+1, 증가값)
range(5) -> 0부터 5-1 4까지 반복

range(1,6) -> 1부터 6-1 까지 반복

range (0,10,2) 0번부터 +2씩 증가해서 9까지 반복

range (10,0,-1) 10번부터 -1씩 거꾸로  0이되기 전까지 반복  즉, 10~1까지 반복

for 숫자하나  in range(시작숫자, 끝나는숫자+1):
    print(숫자하나)

break = 반복을 완전 종료
continue = 건너뛰고 계속 진행
'''


'''
def 기본for문():
    for 숫자하나 in range(5):
        print(숫자하나)


#기본for문()

def 시작_끝_for문():
    for i in range(1,6):
        print(i)
    #1부터 5까지 출력하는 for문 만들기 변수이름 = i

def 시작_끝_2씩_증가_for문():
    for i in range (0,10,2):
        print(i)
    #0부터 9까지 2씩 증가하는 for문 만들기 변수이름 = i

def break_5에서_멈추는_for문():

    #0~9 까지 출력, 5를 만나면 break 변수이름 = i

#def continue_8에서_멈추는_for문():
    for i in range(0,10):
        if i==8:
            continue
    #0부터 9까지 출력 8을 만나면 출력하지 않고 건너뛰어 계속 진행하는 변수이름

def 구구단():
    단 = int(input("단수 를 입력하세요 : "))
    for i in range(1,10):
        print(f"{단} x {i} = {단*i}")



리스트 목록 순회하기
목록들=["포도",'신발',100,'안녕',True]

for i in 목록들:
    print(i)


def 과일들():
    과일리스트=["사과","바나나","포도"]
    for 과일 in 과일리스트:
        print(과일)

#과일들()

def 코드들():
    언어_리스트 = ["C","Java","Python","HTML","CSS","JavaScript"]
    for 언어 in 언어_리스트:
        print(언어_리스트)

코드들()
'''
def 파일만들기():
    title = input("파일이름을 입력하세요 : ")
    filetype = input("확장자를 입력하세요 (txt, py, csv) : ")
    filename= title+"."+ filetype

    with open(filename,"w",encoding="utf-8")as file:
        while True:
            text = input("입력하세요(exit)종료 : ")
            if text.lower()=="exit":
                print(f"{filename} 작성완료")
                break
            file.write(text+"\n")

파일만들기()

def 파일읽기():
    with open("오늘일기.txt","r",encoding="utf-8") as file:
        content = file.read()
        print(content)

파일읽기()