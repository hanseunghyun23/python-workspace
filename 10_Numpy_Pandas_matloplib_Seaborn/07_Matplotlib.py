'''
Matplotlib
- 파이썬의 기장 기본적인 시각화 라이브러리
그래프의 모든 것을 직접 제어할 수 있다

'''
#matplotlib 라이브러리에서 특정 가능 pyplot 를 가지고 와서 그래프를 그릴건데
# 명칭이 너무 길어서 plt 명칭으로 축소해서 부를 것이다
import matplotlib.pyplot as plt
import numpy as np



plt.rcParams['font.family'] = 'D2Coding' #나의 컴퓨터에 없는폰트는 지원x
plt.rcParams['axex.funicode_minus'] = False
# - 만 깨짐 설정 방지하는 이유는 matplotlib 기본 설정이 유니코드 마이너스 기호를 사용하도록
#세팅되어있다
x=[1,2,3,4,5]
y=[2,4,1,5,3]

#기본 선형 그래프
plt.plot(x,y)
plt.title("기본 선 그래프")
plt.xlabel("x축")
plt.ylabel("y축")
plt.show()


#막대 그래프
plt.bar(['A','B','1'],[10,20,15])
plt.show()

#산점도 = 두 변수의 관계를 파악할 때 사용 공부시간, 성적 광고비, 매출
plt.stcatter(x,y)
plt.show()


#히스토그램
data = np.rendn(1000)
plt.hist(data, bins=30)





