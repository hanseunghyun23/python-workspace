'''
java = Map과 유사
Dictionary : 키 : 값 쌍으로 저장하는 것 {"키" : "데이터"}

'''
def Dictionary기초():
    유저정보 = {
        "이름" : "월수",
        "나이" : 25,
        "이메일" : "wallsu@email.com",
        "구독" : True,
    }


    #값 꺼내기
    print(유저정보["이름"])
    print(유저정보["나이"])
    # print(유저정보["전화번호"])
    print(유저정보.get("전화번호","없음"))
    # 있는지 없는지 애매모호한 키의 경우 get() 이용해서
    # get("키이름","키가 없을경우 표기해줄 메시지") 작성해 안전하게 데이터 꺼내기 진행


유저정보["전화번호"] = "010-0000-0000"
유저정보["나이"] = 26
del 유저정보['구독']

#키 이름만 가져오기

#키 이름만 가져오기

#키 이름만 가져오기


for all in 유저정보.items():
    print(f" 유저정보에 있는 데이터 하나씩 모두 꺼내기{all}")

    for 키,값 in 유저정보.values():
        print(f" 유저정보에 있는 데이터 하나씩 모두 꺼내기{all}")


    def 음원스트리밍횟수():
    # 음원 스트리밍 횟수 -> 1000회 이상만 필터
    스트리밍 = {"Dynamite": 500, "Butter": 1500, "DNA": 2000, "Boy With Luv": 800}

    # 1. 기본 for문을 이용해 {"Butter": 1500, "DNA": 2000} 출력
    # 변수이름 =i
                for name, value in 스트리밍.items():
                    if value >=1000:
                        print(f"'{name}' : '{value}'")


    # 2.dict Comprehension {"Butter": 1500, "DNA": 2000} 출력
    #       변수이름 = 인기곡, 곡, 횟수 출력
            인기곡 = {곡: 횟수 for 곡,횟수 in 스트리밍.items() if 횟수>= 1000}
            print(인기곡)
    음원스트리밍횟수()