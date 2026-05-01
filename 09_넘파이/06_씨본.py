'''
Seaborn python 데이터 시각화 라이브러리
matplotlib 기반으로 만들어 졌지만 훨씬 적은 코드로 예쁜 그래프 그릴 수 있다
판다스 DataFrame과 함께 데이터 분석할 때 자주 사용

주 종류
scatterplot : 산점도 분포 파악
lineplot    : 선 그래프 추세 파악
histplot    : 히스토그램
barplot     : 바 그래프 카테고리별 평균
boxplot     : 분포 이상치확인
heatmap     : 색상으로 상관관게

설치 방법
pip install seaborn

'''
import seaborn as sns
import matplotlib.pyplot as plt
import os
#한글 폰트 설정
plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] - False


#seaborn 회사에서 tips.csv와 같은 형태로 데이터가 csv 형태로 보관되있는 데이터를
#seaborn 회사에서 .csv 없이 사용할 수 있도록 코딩세팅을 해놓았으므로
#tips 라는 명칭으로 가볍게 우리가 seaborn 테스트 할 수 있는 것
df = sns.load_dataset("tips")

def 판다스를_이용하여_데이터구조확인():
    print(df.head())
    print("=="*80)
    print(df.shape)
    print("=="*80)
    print(df.columns)
    print("=="*80)
    print(df.dtypes)
    print("=="*80)
    print(df.describe())

판다스를_이용하여_데이터구조확인()

def seaborn에서_만든데이터_내컴퓨터에_csv로_저장하기():
    df.to_csv("seaborn.csv",index=False, encoding="utf-8-sig")
    print("seaborn 에서 만든 데이터 csv로 저장 완료")
    print(f"seaborn_{df}.csv 저장완료")

def seaborn_data_all_save():
    os.mkdir(저장할폴더,exist_ok= True)
    df.to_csv("seaborn.csv",index=False, encoding="utf-8-sig")
    dataset = ["tips", "titanic","iris","penguins","flights","diamonds","mpg"]
    for name in dataset:
        df = sns.load_dataset(name)
        df.to_csv(f"seaborn_{name}.csv 저장완료")

#for문을 이용해 데이터셋 모두 저장하기
seaborn에서_만든데이터_내컴퓨터에_csv로_저장하기()

#저장할 때 마다 seaborn_{name}.csv 저장완료 표기


#seaborn에서_만든데이터_내컴퓨터에_csv로_저장하기()

sns.scatterplot(data=df, x="total_bill",y="tip",hue="sex")
plt.title("계산서 vs 팁")
plt.show()