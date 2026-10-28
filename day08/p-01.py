# 판다스 : 데이터 분석 ( 표형태 ) 라이브러리
# 설치 : pip install pandas
# 호출
import pandas as pd
print( pd.__version__)

# 1] 데이터프레임 : 2차원(표) pd.DataFrane ( 리스트 , colums=['열이름' , '열이름'] )
data_list = [
            [ 'ant' , 25 , 'seoul'] ,
            ['bee' , 30 , 'busan'] ,
            ['cat' , 35 , 'incheon'] ] # 2차원 리스트 ( 대괄호 안에 대괄호 )
x = pd.DataFrame( data_list )
print( x )
# => (numpy와 다르게) 행과 열로된 표 형태로 나옴
x = pd.DataFrame( data_list , columns=['name ' , 'age' , 'city'] )
print( x )
# 2] 데이터프레임2 , pd.DataFrame( 딕셔너리 ) , 키(열이름) / 값(속성값)
data_dict = { 'name' : ['ant','bee','cat'] , 
               'age' : [25,30,35] , 
               'city' : ['seoul','busan','incheon'] } # 딕셔너리
df = pd.DataFrame(data_dict)
print( x )  
# 3] 컬럼 값 추출 , df['열이름'] => 한줄만 추출

# 특정 컬럼(값)만 추출하기
ages = df['age'] # 나이 추출
print( ages ) # Series( 1차원 )
print( type(ages)) # <class 'pandas.Series'>
print( type(ages.values) ) # <class 'numpy.ndarray'>

# 4] 데이터프레임 : 넘파이 -> Pandas 데이터프레임으로 변환이 됨 / 사용처 : 몇몇 프레임워크를 넘파이로 던져주면 그 떄 사용
import numpy as np
data_np = np.array( data_list ) # 넘파이
df = pd.DataFrame(
        data_np , 
        columns= ['name' , 'age' , 'city'] ,
        index = [ 'A' , 'B ' , 'C' ] )
print( df )