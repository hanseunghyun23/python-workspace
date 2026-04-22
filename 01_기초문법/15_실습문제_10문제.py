def 문제1():
    name = "홍길동"
    age = 25
    # 아래처럼 출력되도록 완성하세요
    # 안녕하세요! 저는 홍길동이고 25살입니다.
    print(f"안녕하세요! 저는 {name}이고 {age}입니다. ")
#문제1()

def 문제2():
    name = input("이름을 입력하세요")
    age= int(input("나이를 입력하세요"))
# 이름과 나이를 입력받아서 출력하세요
# 홍길동님은 내년에 26살이 됩니다!
    print(f"{name}님은 내년에 {age+1}살이 됩니다 ")
#문제2()

def 문제3():
    점수 = int(input("점수를 입력하세요: "))
    if(점수>=90):
        print("A")
    # 90이상 A학점
    elif(점수>=80):
        print("B")
    # 80이상 B학점
    elif(점수>=70):
        print("C")
    # 70이상 C학점
    else:
        print("F")
    # 나머지 F학점

#문제3()

def 문제4():

# 숫자를 입력받아서 exit 입력시 종료


    while True:
        i = input("숫자 입력")
        int(i)
        i+=j
        if i=="exit":
            print("합계",i)



# 입력한 숫자들의 합계 출력
# 합계: 60

#문제4()  나중에 ㄱㄱ

def 문제5():
    단 = int(input("단수를 입력하세요: "))
    for i in range(1,10):
        print(f"{단}x{i}={단*i}")

#문제5()

def 문제6():
    과일들 = ["사과", "바나나", "포도"]
    과일들.append("수박")# 수박 추가
    과일들.remove("바나나")# 바나나 삭제
    print(과일들)# 전체 출력
    print(len(과일들))# 과일 개수 출력

 #문제6()

def 문제7():
    언어들 = ["Python", "Java", "JavaScript", "HTML", "CSS"]
    for i,lang in enumerate(언어들):
        print(f"{i+1}번 {lang} ")
    # enumerate 이용해서 1번부터 출력
    # 1번: Python
    # 2번: Java
    # ...

#문제7()

def 문제8():
# 파일이름과 확장자를 input으로 받아서
# exit 입력 전까지 내용 작성
# 작성완료 출력

#문제8()

def 문제9():
# 문제8에서 만든 파일을
# 줄번호와 함께 읽기
# 1번째 줄: 내용
# 2번째 줄: 내용

 #문제9()

def 문제10():
    이름들 = []
    점수들 = []
    # 이름 3개 + 점수 3개 입력받아서 리스트에 저장
    for x in range(0,3):
        name = input("이름을 입력하세요")
        score = int(input("점수를 입력하세요"))

        이름들.append(name)
        점수들.append(score)


    # enumerate 로 번호 붙여서 출력
    # 평균 점수 출력
    # 1번: 홍길동 - 90점
    # 2번: 김철수 - 80점
    # 3번: 이영희 - 70점
    # 평균: 80.0점

문제10()