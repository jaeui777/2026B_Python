# 샘플 데이터
import pandas as pd
raw_data = [
    {'사번': 25001, '이름': ' 김철수 ', '나이': 20.0, '부서': '정보보호부', '입사일': '2022-03-02'},
    {'사번': 25001, '이름': ' 김철수 ', '나이': 20.0, '부서': '정보보호부', '입사일': '2022-03-02'},  # 완전 중복 행
    {'사번': 25002, '이름': '이영희', '부서': '기술부', '입사일': '2021-03-02'},               # 나이 키 누락 (NaN 결측)
    {'사번': 25003, '이름': '박민수', '나이': 22.0, '부서': '', '입사일': '2020-03-02'},      # 부서 빈 문자열 ('')
    {'사번': 25004, '이름': '정수진', '나이': 20.0, '부서': '전략본부', '입사일': '2022-03-02'},
    {'사번': 25005, '이름': '한미래', '나이': 23.0, '부서': '개발부', '입사일': '2019-03-02'},
    {'사번': 25005, '이름': '한미래', '나이': 23.0, '부서': '개발부', '입사일': '2019-03-02'},  # 완전 중복 행
    {'사번': 25006, '이름': ' 강동원 ', '나이': 25.0, '부서': '개발부', '입사일': '2018-07-15'},  # 이름 앞뒤 공백
    {'사번': 25007, '이름': '최유리', '부서': '기획부', '입사일': '2023-01-10'},               # 나이 키 누락
    {'사번': 25008, '이름': '조현우', '나이': 21.0, '부서': '   ', '입사일': '2021-08-20'},    # 부서 스페이스 공백 ('   ')
    {'사번': 25009, '이름': '윤서연', '나이': 24.0, '부서': '인사부', '입사일': '2020-11-05'},
    {'사번': 25010, '이름': ' 송민호 ', '나이': 22.0, '부서': '기술부', '입사일': '2022-05-12'},  # 이름 앞뒤 공백
    {'사번': 25011, '이름': '백지은', '부서': '전략본부', '입사일': '2023-04-03'},             # 나이 키 누락
    {'사번': 25012, '이름': '서동현', '나이': 26.0, '부서': '개발부', '입사일': '2017-09-01'},
    {'사번': 25013, '이름': '신아름', '나이': 21.0, '부서': '', '입사일': '2022-10-18'},      # 부서 빈 문자열
    {'사번': 25013, '이름': '신아름', '나이': 21.0, '부서': '', '입사일': '2022-10-18'},      # 중복 행
    {'사번': 25014, '이름': '오상우', '나이': 23.0, '부서': '정보보호부', '입사일': '2021-02-15'},
    {'사번': 25015, '이름': ' 임지선 ', '나이': 20.0, '부서': '기획부', '입사일': '2023-06-01'},  # 이름 앞뒤 공백
    {'사번': 25016, '이름': '하태웅', '나이': 24.0, '부서': '기술부', '입사일': '2019-12-20'},
    {'사번': 25017, '이름': '문채원', '부서': '개발부', '입사일': '2022-08-01'},               # 나이 키 누락
]

df = pd.DataFrame(raw_data)

df.info()
# 1. 중복 행 제거  , df.drop_duplicates().reset_index( drop=True ) , 
# df = df.drop_duplicates() # 인덱스 유지
df = df.drop_duplicates( ).reset_index( drop=True ) # 인덱스 초기화
# 2. 타입변환 ,  df['컬럼명'].astype( 변환할타입 )
df['사번'] = df['사번'].astype(str)
# 3. 공백 문자( ' ' , '' )는 결측(NaN) 만들기 , 
# 문자열.strip() 앞뒤 여백/공백 제거 함수
# 문자열.replace( '기존문자' , '새로운문자' ) 문자열내 기본문자가 존재하면 새로운문자로 치환
df['이름'] = df['이름'].str.strip()
df['부서'] = df['부서'].str.strip().replace( '' , None )
# 4. 결측치(NaN) 확인 , df.isnull().sum()
print( df.isnull().sum() )
# 5. 결측이 포함된 행/열 자체 제거 , df.dropna( axis=0/1 )
new_df = df.dropna( axis= 0 )
new_df.info()
# 6. 결측값 채우기, df['컬럼명'].fillna() , 표본이 부족 하거나 손실 막기 위해 대표값 채우기( 중앙값(수치), 최빈값(범주) )
# 나이 = 수치/중앙값 , 부서 = 범주/최빈값  
df['나이'] = df['나이'].fillna( df['나이'].median() ) # 이상치 최소화
df['부서'] = df['부서'].fillna( df['부서'].mode()[0] ) # df['컬럼명'].mode()[0] 최빈값
print( df )
# 7. 지징된 임계 범위 기준으로 강제 조정 , 임계범위 벗어나면 최솟값(18)/최댓값(60)으로 조정
df['나이'] = df['나이'].clip( lower=18 , upper=60 ) 

# 8. 연속형 구간 기준으로 범주로 변환 , pd.cut( df['컬럼명'] , bins=[구간범위] , labels=[범주명] )
bins = [ 0 , 20 , 30 , 40 ] # 구간 
labels = [ '청년기' , '도약기' , '성숙기'] # 구간에 따른 범주 정의 
# 0 ~ 20 청년기  / 21 ~ 30 도약기 / 31~40 성숙기
df['연령그룹'] = pd.cut( df['나이'] , bins= bins , labels= labels  )

# 9. 다양한 날짜형식( yyyy-mm , yyyy/mm , yyyy.mm 등 ) 표준 날짜 변환 함수 , pd.to_datetime( )
df['입사일'] = pd.to_datetime( df['입사일'] )
print( df['입사일'].dt.year ) 
# .dt.year 연도 , dt.month 월 , day 일 , day_weekday 요일( 0~6 )
# .dt.hour 시 , dt.minute 분 , dt.second 초

# 10. 그룹화 집계 , df.groupby( ['그룹컬럼명'] )['집계컬럼명'].집계함수()
new_df = df.groupby( '부서' )['나이'].mean() # 부서별 나이 평균 
new_df = df.groupby( ['부서','연령그룹'] )['나이'].mean() # 다중 그룹 
# 다중 집계 ,   .agg( 새로운컬럼명 = ('import pandas as pd

# Python Pandas Practice3
# # 문제 1: 딕셔너리를 활용한 데이터프레임 생성 및 속성 확인
# 아래 딕셔너리(도서관 재고 데이터)를 활용하여 DataFrame을 생성한 뒤,
# 데이터프레임의 행/열 크기(shape), 인덱스 목록(index), 컬럼 목록(columns) 및 요약 정보(info)를 출력하시오.
data_dict = {
    'BookTitle': ['Python Basic', 'Data Analysis', 'AI Agent'],
    'Stock': [15, 8, 23],
    'Location': ['Floor_1', 'Floor_2', 'Floor_1']
}

df = pd.DataFrame(data_dict)
print(df.shape)
print(df.index)
print(df.columns)
df.info()

# 문제 2: loc와 iloc를 이용한 인덱싱 및 슬라이싱
# 아래 데이터프레임에서 loc를 사용하여 'C2'부터 'C3' 행까지의 'Menu'와 'Price' 열을 슬라이싱하여 추출하고,
# 동시에 iloc을 사용하여 1행 2열 위치의 카테고리('Bakery') 값을 추출하여 출력하시오.
df = pd.DataFrame({
    'Menu': ['Americano', 'Croissant', 'Latte', 'Cake'],
    'Price': [4500, 3800, 5000, 6500],
    'Category': ['Coffee', 'Bakery', 'Coffee', 'Dessert']
    }, index=['C1', 'C2', 'C3', 'C4'])
print(df.loc['C2':'C3', 'Menu' : 'Price'])
print(df.iloc[1,2])

# 문제 3: 다중 조건 행 필터링 
# 아래 온라인 쇼핑몰 상품 데이터에서 평점('Rating')이 4.0 이상이면서 동시에
# 리뷰 수('ReviewCount')가 100회 이상인 상품들만 비트 연산자(&)를 사용하여 필터링하고 출력하시오.
df = pd.DataFrame({
    'Product': ['Keyboard', 'Mouse', 'Headset', 'Webcam'],
    'Rating': [4.5, 3.8, 4.2, 4.8],
    'ReviewCount': [150, 80, 210, 45]
}, index=['P1', 'P2', 'P3', 'P4'])

x = df[(df['Rating'] >= 4.0) & (df['ReviewCount'] >= 100)]
print ( x )

# 문제 4: 다중 조건 행 필터링 
# 아래 도서 대여 데이터에서 대여 횟수('RentCount')가 20회 이상이거나 또는
# 반납 지연 일수('OverdueDays')가 5일 이상인 도서 데이터를 비트 연산자(|)를 사용하여 필터링하고 출력하시오.
df = pd.DataFrame({
    'Title': ['Book_A', 'Book_B', 'Book_C', 'Book_D'],
    'RentCount': [12, 22, 15, 25],
    'OverdueDays': [7, 2, 0, 6]
}, index=['B1', 'B2', 'B3', 'B4'])

x = df[(df['RentCount'] >= 20) | (df['OverdueDays'] >= 5)]
print( x )

# 문제 5: 필터링 기준 기존 컬럼 값 수정 
# 아래 학생 평가 데이터에서 'FinalScore'가 90점 이상인 학생의 'Grade'를
# loc 조건식을 사용하여 'A+'로 일괄 수정하고 전체 데이터프레임을 출력하시오.
df = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'FinalScore': [78, 94, 88, 91],
    'Grade': ['B', 'A', 'B', 'A']
}, index=['S1', 'S2', 'S3', 'S4'])
df.loc[df['FinalScore'] >= 90 , 'Grade'] = 'A+'
print( df )

# 문제 6: 필터링 기준 기존 컬럼 값 수정 
# 아래 매장 재고 데이터에서 재고 수량('Stock')이 10개 미만인 상품의 'Status' 컬럼 값을
# loc 조건식을 사용하여 기존 'Normal'에서 'Restock_Needed'로 일괄 변경하고 전체 결과를 출력하시오.
df = pd.DataFrame({
    'Item': ['Pen', 'Notebook', 'Eraser', 'Ruler'],
    'Stock': [25, 6, 40, 8],
    'Status': ['Normal', 'Normal', 'Normal', 'Normal']
}, index=['T1', 'T2', 'T3', 'T4'])

df.loc[df['Stock'] < 10 , 'Status'] = 'Restock_Needed'
print(df)

# 문제 7: 필터링 기준 파생 컬럼 값 수정 
# 아래 회원 실적 데이터에 기본값이 'General'인 'Membership' 컬럼을 추가한 뒤,
# 'TotalSpent'가 300,000원 이상인 회원의 'Membership' 값을 loc 조건식을 사용하여 'VIP'로 변경하여 출력하시오.
df = pd.DataFrame({
    'Member': ['Kim', 'Lee', 'Park', 'Choi'],
    'TotalSpent': [150000, 320000, 450000, 210000]
}, index=['M1', 'M2', 'M3', 'M4'])

df.loc[df['TotalSpent'] >= 300000, 'Membership'] = 'VIP'
print(df)

# 문제 8: 컬럼명 변경 및 통계 집계
# 아래 매장 판매 데이터의 컬럼명 'Units'를 '판매수량'으로, 'Discount'를 '할인율'로 rename을 사용해 변경한 뒤,
# 변경된 '판매수량'의 총합(sum)과 'Grade' 컬럼의 고윳값별 빈도수(value_counts)를 각각 출력하시오.
df = pd.DataFrame({
    'Item': ['Pen', 'Notebook', 'Eraser', 'Ruler'],
    'Units': [120, 45, 80, 30],
    'Discount': [0.1, 0.05, 0.2, 0.0],
    'Grade': ['A', 'B', 'B', 'A']
})
df = df.rename( columns= {'Units' : '판매수량' , 'Discount' : '할인율'})
print( df )
print(df['판매수량'].sum())
print(df['Grade'].value_counts())
# 문제 9: 데이터 연결 (Concat)
# 상반기 지점 실적(df_first)과 하반기 지점 실적(df_second)을 세로(행 방향, axis=0)로 연결하되,
# 기존 인덱스를 무시하고 새롭게 0부터 번호를 매기는 방식(ignore_index=True)으로 연결하여 출력하시오.
df_first = pd.DataFrame({'Code': ['S10', 'S20'], 'Revenue': [500, 750]})
df_second = pd.DataFrame({'Code': ['S30', 'S40'], 'Revenue': [620, 890]})

x = pd.concat

# 문제 10: 데이터 병합 (Merge)
# 회원 기본 프로필(df_user)과 최근 주문 내역(df_order)을 'UID' 기준으로 병합하되,
# 양쪽 모두에 존재하는 주문 회원만 결합하는 방식(inner)과 전체 회원을 모두 유지하는 방식(outer)을
# 각각 수행하여 결측치(NaN) 포함 여부를 비교 출력하시오.
# df_user = pd.DataFrame({'UID': [101, 102, 103], 'User': ['James', 'Emma', 'Lucas']})
# df_order = pd.DataFrame({'UID': [102, 103, 104], 'Amount': [15000, 32000, 21000]}) ' , '집계함수명') )
new_df = df.groupby( '부서' ).agg(  
    인원수=( '사번' , 'count'),
    평균나이 = ( '나이' , 'mean' ) ,
    최고령나이 = ( '나이' , 'max') 
)
print( new_df ) # 부서별 인원수/평균나이/최고령나이 

# 정규화: ( x - 최솟값 ) / (최댓값 - 최솟값 )
# 이유 : 0 ~ 1 범위로 만들기 , 서로 다른 속성들의 간의 이상치/왜곡 방지 
# 예] 나이 : 0 ~ 150   /  연봉 : 0 ~ 3000000000000

# 원-핫인코딩 : pd.get_dummies( df , columns = [ 컬럼명 ] , dtype=int )
# 이유: 범주(문자) 이해할 수 있는 이진(0/1) 로 변환 , 0/1
# 예] 개발부=0 , 정보보호부=1 , 기술부 = 0 
new_df = pd.get_dummies( df , columns= ['부서'] , dtype=int)
print( new_df )