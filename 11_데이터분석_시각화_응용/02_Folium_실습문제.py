import folium
### 서울특별시 종로구 관철동 위도 경도를 검색해 위치 설정하거나
#### 나의 동네 위도 경도로 변경해서 진행
### 주변 카페 3가지의 위도경도를 알아내어, myLocationMap.html 로 생성하기
# TODO 1. 지도 만들기 (내 동네 위도/경도로 바꿔보기)
m = folium.Map(
    location=[37.3942,126.9568],  # 위도, 경도
    zoom_start=12      # 동네 보기 좋은 줌 레벨
)

# TODO 2. 첫 번째 카페 마커
folium.Marker(
    location=[37.4055, 126.9575],
    popup='메가커피',   # 카페 이름
    tooltip='메가커피 안양관양시장점'  # 마우스 올렸을 때 텍스트
).add_to(m)

# TODO 3. 두 번째 카페 마커
folium.Marker(
    location=[37.404,126.9608],
    popup='빽다방',
    tooltip='빽다방 안양관양중점'
).add_to(m)

# TODO 4. 세 번째 카페 마커
folium.Marker(
    location=[37.4048,126.9577],
    popup='투썸',
    tooltip='투썸플레이스 안양관양시장점'
).add_to(m)

# TODO 5. 저장
m.save('myLocationMap.html')  # 파일 이름