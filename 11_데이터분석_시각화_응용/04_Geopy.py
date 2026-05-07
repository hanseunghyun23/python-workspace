'''
주소를 위도/경도로 바꿔주는 라이브러리

pip install geopy

만약 주소 데이터를 가져왔고, 데이터를 확인해보니 위도, 경도가 존재하지 않아
지도에 표기를 할 수 없다
--> 주소를 위도 경도로 변환

주소만 있는 CSV
    ->      geopy 라이브러리 이용해서 위도 / 경도 변환
        ->          Folium 으로 지도에 찍기

    주요 메서드
    - .geocode("주소") = 주소 -> 위도/경도 변경할 때 사용
    - .reverse("위도","경도") = 위도/경도 -> 주소 변경할 때 사용

    주요 속성
    - .latitude = 위도
    - .longitude = 경도
    - .address = 전체주소 문자열 반환
    - .raw  = 딕셔너리 형태로 모든 정보 반환


'''

from geopy.geocoders import Nominatim # OpenStreetMap 기반 무료
from geopy.geocoders import GoogleV3# OpenStreetMap 기반 유료
#from geopy.geocoders import Kakao   카카오처럼 특정 나라 기반 map없읍
# 참고로 한국의 경우 Nominatim 을 이용하는 것 보다 Kakao에서
#무료 API 를 발급받아 사용하는 것이 더 정확

geolocoder_1 = Nominatim(user_agent='test') # Nominatim 지도 서비스를 꺼내 서버에 test 유저라 보낸다
geolocoder_2 = Nominatim(user_agent='김기연')
#user_agent = Nominatim 서버에게 나는 test라는 사람이다 하고 보내는 이름표
#아무 문자열이나 작성해도 된다
location_1 = geolocoder_1.geocode('서울특별시 마포구 월드컵로 72')
location_2 = geolocoder_2.geocode('이상한주소')

print(location_1.latitude)
print(location_1.longitude)

print(location_2.latitude)
print(location_2.longitude)
# AttributeError: 'NoneType' object has no attribute 'latitude'
# 위도 경도가 없는 주소 에러 발생 try 예외처리 해주는 방법도 좋음
# 데이터 전처리를 해도 된다