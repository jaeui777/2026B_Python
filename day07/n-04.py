import numpy as np # 넘파이 호출 
# 1차원 배열 통계 
x = np.array( [1,2,3,4,5] )
print( np.min( x ) )    # 최솟값 
print( np.max( x ) )    # 최댓값 
print( np.argmin( x ) ) # 최솟값 (인덱스)위치
print( np.argmax( x ) ) # 최댓값 (인덱스)위치
print( np.sum( x ) )    # 합계
print( np.mean( x ) )   # 평균 
print( np.median( x ) ) # 중앙값 
print( np.var( x ) )    # 분산 : 요소들의 흩어짐 정도
print( np.std( x ) )    # 표준편차 : 분산의 양의 제곱근 
print( np.sqrt( x ) )   # 루트

# 2차원 배열 통계 함수
# np.통계함수( 2차원배열 , axis = 생략시 1차원 평탄화 , 0열마다, 1행마다)
y = np.array( [ [ 1,2,3] , [4,5,6] ] )
print( np.min( y ) , np.max( y ) ) # 1 6
print( np.min( y , axis=0),  np.max( y , axis = 1) ) # axis = 0 열마다 = 1 행마다
print( np.argmin( y ) , np.argmax( y ) )
print( np.sum( y , axis=0) , np.mean( y , axis=0 ) , np.medain( y , axis=1) )
print( np.var( x ) , np.std( x ) , np.sqrt( x ) )

