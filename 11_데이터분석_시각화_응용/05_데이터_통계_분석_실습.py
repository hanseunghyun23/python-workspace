import pandas as pd
import folium

def sol1():
    # todo 1 : CSV 파일 읽기
    # 힌트 : encoding='cp949' 사용
    df = pd.read_csv('데이터실습파일/노숙인생활시설및생활인원(2015년이후)_20260507123008.csv',encoding='cp949',header=2 )
    # todo 2 : 실제 데이터가 몇 번째 행부터 시작하는지 확인

    # todo 3 : 서울시 전체 말고 자치구별 행만 추출

    # todo 4 : 자치구별 시설 수를 출력
    print()
    # todo 5 : 시설 수가 가장 많은 자치구는 어디인지 출력

sol1()

def sol2():
    # todo 1 : CSV 파일 읽기
    # 힌트 : read_csv 사용, encoding='cp949'

    # todo 2 : 컬럼 확인
    # 힌트 : print(df.columns)
    print(df)
    # todo 3 : 위도 경도 NaN 있는 행 제거
    # 힌트 : dropna(subset=["위도", "경도"])

    # todo 4 : 지도 생성 (성북구 중심)
    # 힌트 : 성북구 위도경도 37.5894, 127.0167
    m = folium.Map(location=[37.5894, 127.0167 ], zoom_start=7)
    # todo 5 : 마커 찍기, 클릭하면 약국명 나오게 하기
    # 힌트 : popup=row["약국명"]
        popup=row["약국명"]
    # todo 6 : html 저장
    # 힌트 : m.save("약국지도.html")
    m.save("약국지도.html")
    # todo 7 : 행정동별로 마커 색깔 다르게 찍어보기
    # 힌트 : folium.Icon(color='red') 오늘 배운 거 있잖아요
    #        행정동 종류 확인은 print(df["행정동"].unique())