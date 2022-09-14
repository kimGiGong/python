# 네이버 뉴스
import requests
from bs4 import BeautifulSoup

url = "https://n.news.naver.com/mnews/article/005/0001552230?sid=105"
headers = {"user-agent":"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
print(response.text)
# print(response.content)

# HTML 응답 페이지 파싱
soup = BeautifulSoup(response.content,'lxml')
title = soup.find('title')
print(title)
print(title.text)

# 이미지 찾기
img_tag = soup.select_one("#img1")
print(img_tag)
print(img_tag['data-src'])

# 이미지 파일 다운 : urllib.request > urlretrieve
from urllib.request import urlretrieve # 함수만 하나 임포트

img_url = img_tag['data-src']
file_name = "news_img.jpg"

# 다운 urlretreive(다운받을데이터 url , 저장 파일 경로)
urlretrieve(img_url, file_name)
























