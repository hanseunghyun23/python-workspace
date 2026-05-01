#넘파이 -> 표그리기
import matplotlib.pyplot as plt
'''
plt.subplots()  : 두 가지 동시에 변환
--- fig : 전체 그림들(액자 자체)
--- ax  : 그래프를 그리는 공간(액자 안 캔버스)


plt.plot 대신 ax.plot() 을 쓰는 것만 다르고 결과는 동일하다

그래프가 1개일 때 
fig,ax = plt.subplots()
ax.plot([1,2,3],[4,5,6])
ax.set_title("제목")
ax.set_xlabel("x축")
ax.set_ylabel("y축")

그래프가 여러 개일 때 
fig,(ax1, ax2) = plt.subplots(행, 열,그래프 전체 화면 사이즈=(가로,세로)
fig,(ax1, ax2) = plt.subplots(1,2)
(1,2) 의 의미는 아래와 같다
-- 첫 번째 숫자1 -- 세로로 몇줄
-- 두 번째 숫자2 -- 가로로 몇 칸 
--1행 2열이면 아래와 같이 배치
-- [ax1][ax2]

fig,((ax1, ax2),(ax3, ax4) = plt.subplots(2,2)
2행 2열
--[ax1][ax2]
--[ax3][ax4]

fig,ax = plt.subplots()
ax.plot([1,2,3],[4,5,6])
ax.set_title("제목")
ax.set_xlabel("x축")
ax.set_ylabel("y축")


plt.plot 대신 ax.plot()을 사용하는 것만 다르고 결과는 동일
'''