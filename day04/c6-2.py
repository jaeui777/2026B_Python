# 예외객체 란? 발생한 예외 정보 갖는 객체
# 예외클래스 : Exception( 예외 최상위 클래스 )
# except 예외클래스명 as 변수명 : 
# as 키워드 : 클래스의 객체변수 생성
# 그외 모든 예외 처리 : 여러개 except 에서 Exception은 항상 마지막에 위치
# 주의할점 : Exception 앞에 위치하면 아래 예외가 작동을 안함.
# PASS : 아직 미구현 / RAISE는 강제로 예외를 발생시킬 때 , 주로 CRUD 안에서 실패 500 의미로도 사용  
# p.383
list_number = [ 52, 273, 32, 72, 100 ]
try :
    number_input = int( input('정수입력 :')) # 타입 예외가 발생 할 수 있음
    print( list_number[ number_input ]) # 인덱스 예외가 발생 할 수 있음
    raise NotImplementedError
    # java : throws new 예외클래스() 
except ValueError as e :                # 타입변환 예외 catch( Exception e ) { }
    print( e )
except IndexError as e :                # 인덱스 예외
    print( e )
except Exception as e :                 # 그외 (최상위) 예외 항상 마지막
    print( e )

    a = 10      #전역스택
    def 함수( ) :
        # global a #단순 호출이면 global 생략가능 , 만약 전역변수를 수정할 거면 global 키워드 꼭 사용
        global a # global 전역변수명
        a = a + 1 
        print( a ) #global 없이도 전역스택 가능
        b = 20 #함수스택
    함수(  )

