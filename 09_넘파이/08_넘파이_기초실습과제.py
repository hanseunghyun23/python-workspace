import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def 배열만들기():
    #1. 0이 6개인 배열을 만들고 출력하세요
    ze = np.zeros(6)
    print(ze)
    #2. 1이 5개인 배열을 만들고 출력하세요
    on = np.ones(5)
    print(on)
    #3. 0부터 30까지 5씩 건너뛰는 배열을 만들고 출력하세요
    print(np.arange(0,31,5))
    #4. 0부터 1까지 균등하게 나눈 값이 8개인 배열을 만들고 출력하세요
    print(np.linspace(0,1,8))



def 배열연산():
    a = np.array([10, 30, 50])
    b = np.array([2, 3, 5])

    #1. a와 b를 더한 결과를 출력하세요
    sum = a+b
    print(sum)
    #2. a에서 b를 뺀 결과를 출력하세요
    str = a-b
    print(str)

    #3. a와 b를 곱한 결과를 출력하세요
    mul = a*b
    print(mul)
    #4. a를 b로 나눈 결과를 출력하세요
    di = a/b
    print(di)
    #5. 일반 파이썬 리스트 [10, 30, 50] + [2, 3, 5] 를 출력하고,
    #NumPy 결과와 어떻게 다른지 주석으로 작성하세요
    a =[10,30,50]
    b = [2,3,5]
    print(a+b) #일반 리스트는 다른 리스트 전체하고 합쳐지는 반면, numpy는 원소들끼리 더해짐

def 인덱싱_슬라이싱_필터링():

    a = np.array([10, 20, 30, 40, 50, 60, 70])
   # 1. 첫 번째 값을 출력하세요
    b= np.a[0]
    print(b)

   # 2. 마지막 값을 출력하세요
   fin = np.a[-1]
   print(fin)
   # 3. 인덱스 2번부터 5번까지 슬라이싱해서 출력하세요
   sl = np.a[2:6]
   print(sl)
   # 4. 40보다 큰 값만 필터링해서 출력하세요
    over = np.a[a>40]
    print(over)
   # 5. 20으로 나누어 떨어지는 값만 필터링해서 출력하세요
    print(a[a % 20 ==0])

def 통계함수():
    scores = np.array([70, 85, 90, 55, 78, 92, 63, 88])

    #1. 점수의 총합을 출력하세요
    m = np.sum(scores)
    print(m)
  #  2. 가장 높은 점수를 출력하세요
    ma = np.max(scores)
    print(ma)
   # 3. 가장 낮은 점수를 출력하세요
    min = np.min(scores)
    print(min)
    #4. 평균 점수를 출력하세요
    avg = np.mean(scores)
    print(avg)
    #5. 표준편차를 출력하세요
    print(np.std(scores))
    #6. 중앙값을 출력하세요
    print(np.median(scores))


def 카페매출분석():
    #아래 배열은 8일간 카페 아메리카노 판매량입니다.

    sales = np.array([30, 15, 42, 27, 38, 19, 50, 33])

    #1. 총 판매량을 출력하세요
    print(np.sum(sales))
    #2. 하루 평균 판매량을 출력하세요
    print(np.mean(sales))
    #3. 가장 많이 팔린 날과 가장 적게 팔린 날의 판매량을 출력하세요
    print(np.max(sales))
    print(np.min(sales))
    #4. 평균보다 많이 팔린 날의 판매량만 필터링해서 출력하세요
    print(sales>np.mean(sales))
    #5. 아메리카노 한 잔 가격이 4500원일 때,
    #각 날짜별 매출 금액 배열을 만들고 출력하세요

    sale = sales*4500

plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False
def 데이터확인():
    df = pd.read_csv("소상공인시장진흥공단_전국_카페_점포수_11_04_2019.csv", encoding="cp949")
    업소수 = np.array(df["업소수"])

   # 1. df.head()로 상위 5개 행을 출력하세요
    print(df.head())
   # 2. df.shape로 행과 열 개수를 출력하세요
    print(df.shape())
   # 3. 업소수 배열을 출력하세요
   print(np.sum)



def 통계분석():
    1. 전체 기간 중 총 업소수 합계를 출력하세요
    print()
    2. 가장 많은 카페가 있던 달의 업소수를 출력하세요
    3. 가장 적은 카페가 있던 달의 업소수를 출력하세요
    4. 월평균 카페 점포수를 출력하세요
    5. 표준편차를 출력하고, 수치가 크면 어떤 의미인지 주석으로 작성하세요
    6. 중앙값을 출력하세요