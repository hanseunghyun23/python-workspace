
def 프로필출력():
    name = "홍길동"
    age = 25
    height = 175.5
    print(name)
    print(age)
    print(height)

프로필출력()

def 나이계산기():
    name = input("이름을 입력하세요")
    birth = int(input("태어난 연도를 입력하세요"))
    age = 2026-birth
    print(f"{name}님의 나이는 {age}입니다")

나이계산기()

def 학점계산기():
    score = int(input("점수를 입력하세요: "))
    if score >= 90:
        print("A")
    elif score >=80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("F")

학점계산기()


def 파일저장():
    with open("result.txt", "w", encoding="utf-8") as file:
        while True:
            text = input("입력하세요 (exit 종료): ")
            if text.lower() == "exit":
                print("저장완료")
                break
            file.write(text + "\n")

    def 파일읽기():
        count = 1
        with open("result.txt", "r", encoding="utf-8") as file:
            while True:
                line = file.readline()
                if line == "":
                    break
                print(f"{count}번째 줄: {line.strip()}")
                count += 1

        # 실행
        print("=== 파일 저장 ===")
        파일저장()
        print("\n=== 파일 읽기 ===")
        파일읽기()