# 설치1 : pip install requests
# 설치2 : pip install beautifulsoup4

# 1] 네이버 검색 정보 크롤링( 정적 )
# 1. 크롤링 주소 가져오기 , "파라미터 정리" , ?쿼리스트링

# 2. requests 라이브러리로 해당 주소 요청하기
url = "https://search.naver.com/search.naver?&query=안양날씨"
import requests                         #

response = requests.get( url ) # requests.get( "요청할 주소" )
# print( response ) # <Response [200]> # HTTP CODE : 200 ( 통신 정상 뜻 )
# print (response.text) # 요청한 주소의 HTML 문자로 반환
# 3. 요청 성공했으면 요청한 페이지의 HTML 파싱 하기
from bs4 import BeautifulSoup # 요청된 URL의 HTML 파싱 라이브러리
# BeautifulSoup( 요청한결과의내용물 , "html.parser")
soup = BeautifulSoup( response.text , "html.parser" )
# print( soup )

# 4. 파싱한 이유 : 특정한 식별자(마크업)의 텍스트/정보 추출
# soup.select( 선택자 )

text = soup.select_one(".temperature_text")
print( text )

# 5. 마크업 사이에 텍스트 추출
# 추출한DOM.get_text() :
print( text.get_text() )