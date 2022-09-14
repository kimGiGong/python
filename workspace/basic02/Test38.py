'''
* 크롤링 Crawling *
    크롤러 : 알고리즘에 의해 인터넷을 탐색하는 프로그램. 스크랩퍼, 봇, 스파이더, 지능에이전트 라고도 함.
    크롤링 : 크롤러가 데이터를 수집하는 행위. 스크래핑

    웹
    클라이언트 : 서비스를 요청하는 프로그램
    서버 : 서비스를 제공해주는 프로그램
        종류
            영상제공, 파일, 도메인, 채팅 및 음성, 게임, 전자우편, 웹 서버.....

    # 헤더
    서버와 클라이언트 간에 데이터를 주고 받을 때, 헤더라는 정보를 포함해서 보낸다.

    요청 헤더 : 클 -> 서버 요청할 때 정보 포함한 헤더
            User-Agent(브라우저 정보), Method(요청 메서드), refered(이전에 머물던 주소)

    응답 헤더 : 사바 -> 클 응답해줄 때의 정보 포함한 헤더
            Status-code (응답 코드)

    일반 헤더 : 양측 모두에서 사용되는 일반 정보 포함된 헤더

    엔티티 : 메세지에 해당하는 정보를 포함하는 헤더
             Content-Type(entity-body의 미디어 타입)

# 크롤링
    웹에 접속해서 데이터를 받아오는 것
    1 - 웹 페이지 요청 -> 요청 라이브러리 (urllib, requests)
    2 - 요청 결과를 파이썬에서 쉽게 사용 가능한 형태로 변환(파싱) -> 라이브러리 (BeautifulSoup)

# requests 라이브러리
    웹 페이지 요청하는 라이브러리
    - requests 검색 + 설치

# BeautifulSoup 라이브러리
    라이브러리 추가 : bs4 검색 + install
    웹 문서 구조로 파싱해주는 라이브러리

    # 파서 종류
        - lxml (HTML parser) : BeautifulSoup(html, 'lxml')
                C 언어로 구현되어 매우 빠름. 라이브러리 추가 필요 (lxml 검색 + 추가)
        - lxml (XML parser) : BeautifulSoup(html, 'lxml-xml')
                매우 빠름, 유일하게 지원되는 xml parser
        - html5lib : BeautifulSoup(html, 'html5lib')
                웹 브라우저 형태로 HTML 을 분석하고 관리, 유효한 HTML5 생성
                라이브러리 추가 필요, 매우 느림
        - html.parser : BeautifulSoup(html, 'html.parser')
                적당한 속도, 라이브러리 추가X
'''
import requests
from pprint import pprint # 데이터 정렬

url = "http://www.naver.com"
res = requests.get(url)
print(res)
print(res.status_code)
pprint(res.headers)
print(res.cookies)

print("*-*-"*10)
# html 코드
# print(res.text)    # Text
print(res.content) # 한글을 바이너리 형태로 가져옴 -> text로 가져올때 한글이 깨지는 경우 content
print("*-*-"*10)
print(res.encoding)



# 2. 요청시 데이터 보내기

# .get() : GET 요청
res = requests.get(url, params={"key1" : "value1" , "key2":"value2"})
print(res.url)

# .post() : POST 요청     params : 쿼리스트링 , body : data 인자 보내기
res = requests.post(url, data={"key1" : "value1" , "key2":"value2"})
print(res.url)
# -> 간혹 정상적인 요청이 안될 경우가 있다.

# 딕셔너리 형태를 유지한 문자열 형태로 데이터 전달 -> json!!!
import json
res = requests.post(url, data=json.dumps({"key1" : "value1" , "key2":"value2"}))
print(res.headers)


'''
# requests 오류 처리 방법
    HTTPError
    ConnectionError
    ProxyError
    SSLError    : SSL 인증서 오류 (https)
    Timeout
    ConnectTimeout
    URLRequired
    TooManyRedirects
    MissingSchema   : HTTP 또는 HTTPS 를 생략했을 때 
    InvalidURL
    ContentDecodingError
    등등

'''
try:
    url = "naver.com/test"
    response = requests.get(url)
    print(response.url)
except requests.exceptions.HTTPError:
    print("HTTP 에러 발생")
except requests.exceptions.Timeout:
    print("Timeout 에러 발생")
except requests.exceptions.MissingSchema:
    print("Missing Schema 발생... url에 http 프로토콜 확인")


# 3. 응답 결과 파싱
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title class="t" id="tid">test title</title>
    </head>
    <body> 
        <p> HAHAHAHAHAHA </p>
        <p> HAHAHAHAHAHA </p>
        <p> HAHAHAHAHAHA </p>
    </body>
</html>
"""


soup = BeautifulSoup(html, 'lxml')
print(soup)
print(type(soup))

print("=" * 50) ######################################## 9월 13일 ####################################
# 태그 접근 #1. soup.태그명
title = soup.title
print(title)      # 내부의 하위 태그들 텍스트도 모두 가져옴
print(title.text) # 정확히 태그에 대한 값만 가져옴
print(title.name) # 태그명

# 태그의 속성 접근
print(title.attrs)  # 딕셔너리 타입
print(title['class'])
print(title['id'])
# print(title['name']) 없는 속성을 꺼내면 에러발생!!
print(title.get('name'))  # get을 사용하면 없으면 None이 나옴 좀더 안전하다
print(title.get('class'))
print(title.get('id'))

# 자식 태그 접근 : contents, children
html = """
<html>
    <head>
        <title class="t abc" id="tid">test title</title>
    </head>
    <body> 
        <p><span>AAAA</span><span>BBBB</span></p>
    </body>
</html>
"""
soup = BeautifulSoup(html, 'lxml')
p_tag = soup.p
print(p_tag)
# print(p_tag.text)
# print(p_tag.string) # p태그가 온전히 가지고있는 text가 없어서 None

children = soup.p.contents
print(children)
children = soup.p.children # 이터레이터로 리턴 -> 반복문으로 꺼내서 사용
print(children)
for child in children:
    print(child)

print("=" * 100)
# 부모태그 접근
span_tag = soup.span
print(span_tag)
print(span_tag.parent)
title(soup.title)
print(title.parent)

# parents : 최상위 부모까지 가져오기
print("=" * 100)
print(span_tag.parents)
for p in span_tag.parents:
    print(p)

# 형제 태그 접근 : next_sibling, previous_sibling
span_tag = soup.span
print(span_tag)
b = span_tag.next_sibling   # 다음 형제
print(b)
a = b.previous_sibling      # 이전 형제
print(a)

# 다음, 이전 요소 접근 : next_element, previous_element
html = """
<html>
    <head>
        <title class="t abc" id="tid">test title</title>
    </head>
    <body> 
        <p>
            <a>AAAA</a>
            <b>BBBB</b>
            <c>CCCC</c>
        </p>
    </body>
</html>
"""
print("=" * 100)
soup = BeautifulSoup(html, 'lxml') # html 바뀌면 요거 써서 새로잡아줘야함
a = soup.a
print(a)
print(a.next_elements)
for n in a.next_elements:
    print(n)
print(a.next_sibling)
















