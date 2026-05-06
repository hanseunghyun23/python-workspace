'''
Pandas - 파이썬에서 표(테이블) 형태의 데이터를 다루는 라이브러리
엑셀과 비슷하다고 생각하면 된다

pip install pandas

기본 사용법
import pandas as pd
* as = alias = 별명, 별칭
import pandas 작성해도 되지만 pandas가 댕길어서 pd라는 이름으로 줄여서 사용하겠다

# 파일 불러오기 기본 인코딩 형식 encoding="utf-8" 기본값으로 작성 안해도 된다
# pd.read_csv("파일이름.csv")

#파일에 내용 작성하기

df = pd.DataFrame(dict(데이터형식))
df.to_csv("만들파일이름.csv")
to_csv 와 같은 형식으로 만들 때에는 컬럼의 이름들과 각 컬럼에 들어갈 데이터를 설정 해주어야 한다
'''

import pandas as pd
from pandas.conftest import index

#df = pd.read_csv("행정안전부_착한가격업소_현황_20260331.csv")
# 보통 한국에서 만든 csv파일은 cp0949 = 한국버전 한국어-> 컴퓨터언어 상호작용 형태로 파일이 만들어진다

#cp949 = EUC-KR
df = pd.read_csv("행정안전부_착한가격업소_현황_20260331.csv", encoding="cp949")

def  데이터기본정보조회():

    헤드 = df.head() #상위 5개의 행 갖고오기 -> 기본으로 출력이 없어서 상위 5개의 행을 보고싶다면 print() 이용함
    print("상의 5개의 행 : ",헤드)
    꼬리 = df.tail() #하위 5개의 행 갖고오기
    # -> 기본으로 데이터를 갖고오는 것이지 출력이 없어 print()이용해 어떤 데이터를 갖고왔는지 확인
    print("아래 5개의 행 : ", 꼬리)

    ### head() 와 tail() 소괄호 안에 숫자를 작성하지 않으면 기본으로 5개 1~n개 작성가능

    헤드_10개 = df.head(10) #상위 5개의 행 갖고오기 -> 기본으로 출력이 없어서 상위 5개의 행을 보고싶다면 print() 이용함
    print("상의 5개의 행 : ",헤드_10개)
    꼬리_20개 = df.tail(20) #하위 5개의 행 갖고오기
    # -> 기본으로 데이터를 갖고오는 것이지 출력이 없어 print()이용해 어떤 데이터를 갖고왔는지 확인
    print("아래 5개의 행 : ", 꼬리_20개)

    csv_정보= df.info() # 데이터 타입, 결측치 확인
    print("csv 정보 : ", csv_정보)

    csv_요약정보=df.describe()# 평균, 최소, 최대 등 통계 요약
    print("csv 요약정보 : ",csv_요약정보)

    행과열의개수 = df.shape
    print("행과 열의 개수 : ",행과열의개수)


'''
데이터 정제
다수 컬럼에서 필요한 열만 뽑거나 특정 조건에 맞는 행만 남기는 행위

열 선택하기
모든 정보가 다 필요하지 않을 때 원하는 컬럼만 리스트 형식으로 가져온다

'''

#df = pd.read_csv("행정안전부_착한가격업소_현황_20260331.csv", encoding="cp949")

def 데이터정제조회():
    #업소명 시도명 품목 가격 컬럼만 따로 저장
    df_컬럼들 = df[['업소명','시도','메뉴1','가격1']]
    df_컬럼 = df['업소명']
    print(df_컬럼들.head()) #원하는 컬럼의 상위 5개만 조회가능
    print(df_컬럼.head()) #원하는 컬럼의 상위 5개만 조회가능
    #KeyError: "['시도명', '품목', '가격'] not in index"
    #특정 조건으로 필터링하기
    #예를 들어 시도명에서 서울특별시인 데이터만 조회
    시도명_서울  = df[df['시도'] =='서울특별시']
    print("서울 소재 업소 수 : ", len(시도명_서울))

'''
결측지 = 데이터가 없는것
0 + " = 컴퓨터 에러 발생 0이랑 빈값이랑 어떻게 더함?
1 + NaN = 뭐하라는 거지? 난 할 수 없어 멐퓨터 에러 발생

NaN = 값이 없음(빈칸)이라는 표시기법
'''


def 데이터결측치정리_조회():
    # df = csv 파일에서 isnull() 빈칸인게 있나요?  .sum 총 몇개죠?
    데이터가_없는_개수확인 = df.isnull().sum
    print("데이터가 없는 개수 확인 : ", 데이터가_없는_개수확인)
    # drop 삭제할게 na Nan 값을            NaN 빈값으로 되어있는 칸 삭제
    데이터가_없는_행삭제 = df.dropna()
    print("데이터 없는 행 삭제 :",데이터가_없는_행삭제)
    #              na NaN 값을 0으로 채워넣겠다 계산하기 편하게
    데이터가_없는_행_0으로_채우기 = df.fillna(0)
    print("데이터 없는 행 0으로 채우기 :",데이터가_없는_행_0으로_채우기)
    데이터가_없는_행_없음으로_채우기 = df.fillna("없음")
    print("데이터 없는 행 평균값으로 채우기 :", 데이터가_없는_행_없음으로_채우기)
    데이터가_없는_행_평균값으로_채우기 = df.fillna(df.mean(numeric_only=True))
    print("데이터 없는 행 평균값으로 채우기 :", 데이터가_없는_행_평균값으로_채우기)

데이터결측치정리_조회()
#데이터정제조회()

def 배열_1차원배열_2차원배열():
    #Series 1차원 배열
    s = pd.Series([10,20,30],index=['a','b','c'])
    #DataFrame 2차원 배열
    #dict은  {}축약형으로
    #df_dict 와 df_중괄호 는 같은 결과 같은 의미 같은 뜻으로 작성 방식만 다르다.
    df_dict = pd.DataFrame(dict(
        name=['Alice','Bob','Charlie'],
    age=[25,30,35],
    score = [90,85,92]

    ))
    df_중괄호 = pd.DataFrame(
        {
        'name':['Alice','Bob','Charlie'],
        'age':[25,30,35],
        'score' : [90,85,92]
        }
    )
    #대부분의 데이터 구조는 다차원 구조

def 머지_콘캣_피벗테이블():
    df1 = pd.DataFrame(
        dict(
            id=[1,2,3],
            name=['A','B','C']
        )
    )

    df2 = pd.DataFrame(
        dict(
            id=[1,2,3],
            name=[90,85,92]
        )
    )
    # 개별로 존재하는 테이블 합치기
    #SELECT
    #FROM 가게 s, 주문 o
    #   판다스에서 합치기 기능을 가져와 사용하겠다 .merge(df1,df2,on='id') 1번 테이블과 2번 테이블을 합칠건데
    #                                                                       두 컬럼에 동일하게 존재하는 컬럼이름 작성)
    #WHERE s.id = 0.id
    합치기 = pd.merge(df1,df2,on='id') #SQL JOIN 문처럼 합칠 기분이 되는 컬럼 설정
    print(합치기)

    df_a = pd.DataFrame(
        dict(
            name=['A','B']
        )
    )

    df_b = pd.DataFrame(
        dict(
            name=['C','D']
        )
    )
    #pd         .concat([df_a,df_b], ignore_index=True)
    #pd.concat([df_a,df_b], ignore_index=True)
    result = pd.concat([df_a,df_b], ignore_index=True)
    result = pd.concat([df_a,df_b]) #igonre_index=False 가 기본값 데이터 그대로 유지하면서 합치도록



머지_콘캣_피벗테이블()

def 필터링_정렬_그룹화():
    #필터링  : 조건으로 행 추려내기


    df[df['컬럼이름']>=30] #특정 컬럼에서 29이하인 데이터 컷

    #여러 조건 (& | 사용)


def 피벗테이블():
    #데이터에서 피벗이란
    #데이터를 출 중심으로 회전시켜 보는 각도를 다르게 하겠다


    df.pivot_table(
        values='score',
        index='name',
        columns='subject',
        aggfunc='mean'
    )
    #index = 왼쪽에 세울 것 columns = 위에 펼칠 것 values = 안에 채울 데이터

def 피벗테이블예시():
    df.pd.DataFrame(
        dict(
            name=['Alice','Alice','bob','bob'],
            subject=['math','eng','math''eng'],
            score = [90,85,80,75]
        )
    )
    print("============피벗 전 데이터 확인===============")
    print(df)

    피벗작업 = df.pivot_table(
        values = 'score',
        index='name',
        columns='subject',
        aggfunc='mean'
    )
    print(피벗작업)
    print("============피벗 후 데이터 확인 ==============")
