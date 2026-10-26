# p.484 클래스변수 ? 인스턴스 없이 사용 가능한 변수
# 클래스 변수명 = 초기값
# Static : 객체 공유가 가능해짐 
class Student2 :
# p.484 클래스변수 ? 인스턴스없이 사용 가능한 변수
# 클래스변수명 = 초기값

count = 0
students = [ ]

# p.486 클래스함수
@classmethod #클래스함수 정의하는 데코레이터/어노테이션
def print( cls ) : # 매개변수에 cls 관례적으로 선언
    for student in cls.students : #cls.클래스변수 <-- 동일--> 클래스명.클래스변수
        print( str(student) )


def __init__(self, name , korean, math , english , science ) :
    # 멤버/인스턴스 변수
    self.name = name
    self.korean = korean
    self.math = math
    self.english = english
    self.science = science
    Student2.count += 1
    Student2.students.append( self )

    class Circle :
        def __init__( self , radius ) :
            self.__radius = radius # java : private in radius
            self.__radius2 = radius # 프라이빗변수
        def get_circumference( self ) :
            return 2* self.__radius # 클래스 내부에서 프라이빗 변수 사용 가능
        # getter and setter
        def get_radius( self ) :
            return self.__radius # 프라이빗 변수 바환하는 getter함수
        def set_radius( self , radius ) :
            self.__radius = radius # 매개변수값을 프라이빗 변수에 저장하는 setter 함수

        @property #게터
        def radius2( self ) :
            return self.__radius2
        @radius2.setter #세터
        def radius2( self, value ) :
            self.radois2 = value
circle = Circle( 10 )
# print( circle.__radius ) # 클래스 외부에서 프라이빗 변수 사용 안됨 
print( circle.get_radius() ) # 10
circle.set_radius( 20 )
print( circle.get_radius() ) # 20
print( circle.radius2 ) # 10
circle.radius2 = 20
print( circle.radius2 ) # 20

# p.497 상속의 활용
class Parent : 
    def __init__(self) :
        self.value = "테스트"
        print( "init 메소드 호출" )
    def test( self ) :
        print( "test()메소드 호출")
#class 자식클래스명( 부모클래스명1 , 부모클래스명2 ) : 파이썬은 부모클래스가 여러개 가능! 
class Child( Parent ) : # java: class 자식클래스명 extends 부모클래스명{ }
    def __init__(self) :
        super().__init__()
        print( ' child init 메소드 호출' )
child = Child()         # print() 출력되는 횟수 # 자식이 태어나면 부모도 같이 태어난다 (1) (3)
child.test()        # (4)
parent2.test()
parent2.test()