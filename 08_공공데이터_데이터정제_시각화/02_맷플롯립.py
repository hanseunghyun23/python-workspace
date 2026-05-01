'''
파이썬에서 그래프/차트를 그리는 라이브러리 데이터를 눈으로 볼 수 있게 해준다

설치방법 pip install matplotlib
선그래프 막대그래프 파이그래프 산점도

plt.plot()(
    x,                      #x축 값(필수)
    y,                      #y축 값(필수)
    color="",               #선 색상(선택)
    linewidth=숫자,         #선 두께(선택)
    linestyle="--",         #선 스타일 -= 실선 -- = 점선 :=점점선
    marker = "o",           #꺾이는 점의 모양
    label="표기이름"        #표기 이름

)
plt.bar(
x,                      #x축 값(필수)
    edgecolor = "',     #막대색상(선택)
    color="",               #선 색상(선택)
    width=숫자,         #막대 두께 기본으로 0.8 세팅(선택)
    alpha=0.7 ,          #막대 불투명도 0~1
    label="표기이름"        #표기 이름
)
plt.pie(
x,                      #데이터 값(필수)
    colors="",               #선 색상(선택)
    autopct="%1.1f%%"           #퍼센트 표시(소수점 1자리) (선택)
   explode=[0.1,0,0]         #선 두께(선택)
    shadow = True           #그림자효과(선택)

    startangle=90        #시작 각도
)
plt.scatter(
x,                      #x축 값(필수)
y,                      #y축 값(필수)
   s=100,               #검 크기선택)
   c=blue               #점 색상(선택)
  alpha=0.5,      #투명도(선택)
  marker="o"        #점 모양 o=원 ^ =삼각형 s=사각형 *=별(선택)

)
plt.hist()
'''


####기본 구조######
import  matplotlib.pyplot as plt

#한글 깨짐 방지 한글 폰트 세팅
#rdParam = 환경설정 설정값들
# rc     = RuntimeConfiguration(실행하는 도중의 설정)
#Params   = Parameters(매개변수, 설정값들)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False #마이너스 기호 깨짐 방지

# plot = 선그래프
plt.plot([1,2,3],[4,5,6])
plt.title("제목")
plt.show()
#bar = 막대그래프
plt.bar(["A","B","C"],[30,50,20])
plt.title("항목별 비교")
plt.show()
#pie = 원형그래프
plt.pie([40,30,20,10],labels=["A","B","C","d"],autopct="%1.1f%%")
plt.title("비율차트")
plt.show()
# scatter = 산점도 관계 확인할 때
plt.scatter([1,2,3,4],[10,20,15,30])
plt.title("두 변수의 관계")
plt.show()







