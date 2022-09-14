from bs4 import BeautifulSoup


html = """
<html>
    <head>
        <title class="a" id="tid">test title</title>
    </head>
    <body> 
        <p>AAAAA1111</p>
        <p id ='a' class='a'>BBBB2222</p>
        <p class= 'b'>CCCCC3333</p>
    </body>
</html>
"""

soup = BeautifulSoup(html , 'lxml')

# 원하는 요소 정확히 접근하기
# find_all()
print(soup.find_all('title'))
print(soup.find_all('p'))
# id 속성값
print(soup.find_all(id='a'))
print(soup.find_all(id=True))
print(soup.find_all(id=False))

print("태그 , id 속성값")
print(soup.find_all('p',id='a'))
print(soup.find_all('p',id='c')) # 태그가 없는경우


# class 속성값
print("class 속성값")
print(soup.find_all(class_="a"))
print(soup.find_all('p',class_="a"))

print(soup.find_all('p',limit=2))
print(soup.find_all('p',limit=4)) # 없어도 있는만큼


# 리스트 형태로 태그명 여러개 검색
print("리스트 형태로 태그명 여러개 검색")
print(soup.find_all(['title','p']))

# 응용 : 두번 거르기
print("응용 : 두번 거르기")
body_tag = soup.find_all('body')
print(body_tag)
print(body_tag[0].find_all('p'))

# find() : 하나의 요소만 가져옴. -> 문서상에 요소가 하나만 존재할 경우 사용하는 것이 좋다.
print("find() 의사용")
print(soup.find('p'))

# select() : CSS 셀렉터를 이용하여 원하는 요소 리스트로 리턴받을 수 있다.
print("select() 의 사용")
html = """
<html>
    <head>
        <title class="a">test title</title>
    </head>
    <body> 
        <p class="a">AAAAA1111</p>
        <p class='b' id ='p' >BBBB2222</p>
        <p class='b'>CCCCC3333</p>
        <a href="/example/test01">a tag</a>
        <b>b tag</b>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'lxml')
print(soup.select('p')) # 태그명
print(soup.select('.a'))
print(soup.select('.b'))
print(soup.select('#p'))
print(soup.select('p#p')) # 태그명#id값 태그명.클래스값

print(soup.select('body .a'))

# extract() : 태그 제거
print("extract() 의 사용")
p_tag = soup.select('p')
print(p_tag)
for p in p_tag:
    print(p.extract())
print(soup)














