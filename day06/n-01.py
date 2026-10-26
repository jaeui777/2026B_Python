#  1. 넘파이 설치 , 터미널 : pip install numpy
#  2. 넘파이 불러오기
# import 라이브러리이름
# import 라이브러리이름 as 별칭
import numpy as np
print( np.__version__)
#  3. 넘파이 학습하는 이유 : 1) 데이터분석(수치계산) 2) ML/DL 라이브러리들이 사용

# 1] 배열 생성
x= np.array( [1, 2, 3, 4])
print( x )
x = np.array( [[1,2,3],
               [4,5,6]
               ]
) # 2차원 배열
print( x )
# [[1 2 3]
# [4 5 6]]]
# 특징1 : 동적(자동으로 타입 정해주는) 타입 느리다. 넘파이는 정적타입 빠르다.
# int a = 10 : 정적타입 , a = 10 동적타입
x = np.array( [ 1 , True , "안녕" ] )
print( x ) # ['1' 'True' '안녕']

# 2] 0 으로 배열 초기화 , .zeros( (행개수 , 열개수))
x = np.zeros( (2,3) ) #
print( x )
#[[0 0 0]
# [0 0 0]]

# 3] 1으로 채워진 배열로 초기화
x = np.ones( ( 2,3 ) )
print( x )

# 4] range( 시작인덱스 , 끝인덱스, 단계 )
x = np.arange( 0 , 10 , 2 )
print( x )

# 5] linespace( 시작값, 끝값 , 사이범위 )
x = np.linspace( 0 , 1 ,5 )
print( x ) 

# * 넘파이는 리스트 또는 튜플 타입의 자료들을 넘파이 타입으로 변환 가

# 6] 배열
x = np.array( [ [1,2,3] , [4,5,6] ] ) #2차원
print( x.shape )

# 7] 배열 타입 확인
x = np.array( [ 1.0 , 2.0 , 3.0 ] )
print( x.dtype ) # float64

# 8]
x = np.array( [ [ [1],[2] ] , [ [2],[3]] , [ [3],[4]] ] )
print( x.size )  # 요소/자료 개
print ( x.ndim ) # 차원수

# 9] 배열의 데이터 타입 , np.array( 리스트/튜플 , dtype=np.타입)
x = np.array( [1,2,3] , dtype=np.int32)
print( x.dtype )
x = np.array( [ 1.0 , 2.0 , 3.0 ] , dtype=np.float32)
print(x.dtype)


# 10] xkdlqqusgshks