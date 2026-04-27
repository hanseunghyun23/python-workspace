import tkinter as tk

def 실습과제1():
    창 = tk.Tk()
    창.title("인사 프로그램")
    창.geometry("300x150")

    # 라벨 (안내 텍스트)
    tk.Label(창, text="이름을 입력하세요:").grid(row=0, column=0, padx=10, pady=10)

    # 입력창
    이름입력 = tk.Entry(창, width=15)
    이름입력.grid(row=0, column=1)

    # 결과 라벨
    결과 = tk.Label(창, text="이름입력", font=("D2Coding", 13))
    결과.grid(row=2, columnspan=2, pady=10)

    # 인사 함수
    def 인사():
        이름 = 이름입력.get()         # 입력창에서 값 꺼내기
        결과.config(text=f"안녕하세요, {이름}님!")  # 라벨 텍스트 변경

        # 버튼
    tk.Button(창, text="", command=인사).grid(row=1, columnspan=2, pady=5)

    창.mainloop()   # 창 유지

def 실습과제2():

    창 = tk.Tk()
    창.title("BMI 계산기")
    창.geometry("300x200")

    # 키 입력
    tk.Label(창, text="키 (cm):").grid(row=0, column=0, padx=10, pady=5)
    키입력 = tk.Entry(창, width=10)
    키입력.grid(row=0, column=1)

    # 몸무게 입력
    tk.Label(창, text="몸무게 (kg):").grid(row=1, column=0, padx=10, pady=5)
    몸무게입력 = tk.Entry(창, width=10)
    몸무게입력.grid( row=1, column=1)

    # 결과 라벨
    결과 = tk.Label(창, text="결과:", font=("D2Coding", 14))
    결과.grid(row=3, columnspan=2, pady=10)

    # BMI 계산 함수
    def BMI계산():
        try:
            키 = float(키입력.get()) / 100     # cm → m 변환
            몸무게 = float(몸무게입력.get())

            bmi = 몸무게/ (키 ** 2)          # BMI 공식
            bmi = round(bmi, 1)              # 소수점 1자리

            if bmi < 18.5:
                판정 = "저체중"
            elif bmi < 22.9:
                판정 = "정상"
            elif bmi < 24.9:
                판정 = "과체중"
            else:
                판정 = "비만"

            결과.config(text=f"BMI: {bmi} → {판정}")

        except ValueError:
            결과.config(text="숫자만 입력하세요!")

    # 버튼
    tk.Button(창, text="계산하기", command=BMI계산).grid(row=2, columnspan=2, pady=5)

    창.mainloop()

실습과제1()