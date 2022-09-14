# 네이버 웹툰

import requests
from bs4 import BeautifulSoup
from pprint import pprint # 콘솔에 예쁘게 출력(줄간격 맞춰서)

headers = {"user-agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

html = requests.get('https://comic.naver.com/webtoon/weekday',headers=headers)
# print(html)
soup = BeautifulSoup(html.content, 'lxml')

# 1. 월요일 제목들 가져오기
'''
<div class="list_area daily_all"> 전체 요일 블럭
    <div class="col"> 요일 하나 * 7
        <div class="col_inner">
            <h4>월요일</h4>
            <ul>
                <li>
                    <div class="thumb">
                        <a href="웹툰페이지경로">
                            <img title="웹툰제목" src="웹툰이미지경로"/>
                        </a>
                    </div>
                    <a href="웹툰페이지경로" class="title" title="웹툰제목">웹툰 제목</a>
                </li> 
                <li>...</li>   웹툰한개
                <li>...</li>
                <li>...</li>
                ...
            </ul>
        </div>
    </div>
</div>
'''
mon = soup.find('div',{'class':'col_inner'})  # 첫번째 요소 한개만 가져옴 -> 월요일
# print(mon)
titles = mon.find_all('a','title')
# pprint(titles)

# 제목만 따로 저장
title_list = []
for t in titles:
    title_list.append(t.text) # 리스트에 저장

pprint(title_list)

# 2. 모든 요일 제목들 가져오기

data = soup.find_all('div',{'class':'col_inner'}) # 전체 요일 기둥들
# pprint(data)
# print(len(data))
week_title_list = []
for day in data:
    d_titles = day.find_all('a','title')
    # pprint(d_titles)
    title_lists = [t.text for t in d_titles] # 요일 한개의 제목 리스트
    week_title_list.append(title_lists) # 전체요일 리스트에 요일한개 리스트 추가

# pprint(week_title_list)
print(len(week_title_list))


# 썸네일 이미지 저장
from urllib.request import urlretrieve # 이미지 저장용 lib
import os, errno    # OS 통해 폴더생성, 예외처리용
import re

'''
os.path.isdir : 이미 디렉토리가 있는지 검사
os.path.join  : 현재 경로를 계산하여 입력한 경로 문자열을 합하여 새로운 경로 만듬
os.makedirs   : 지정한 경로로 폴더 생성

'''
try:
    if not(os.path.isdir('image')): # 현재 위치에 image라는 이름의 폴더가 없으면~
        os.makedirs(os.path.join('image'))  # 만들어라(경로는 image 를 포함한 실제 경로 계산시켜서)
except OSError as e :
    if e.errno != errno.EEXIST: #
        print("폴더생성 실패...")
        exit() # 프로그램 강제종료

# 월요일
img_tag = mon.find_all('img')
# pprint(img_tag)

for img in img_tag:
    title = img['title'] # 웹툰 제목
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title) # 숫자 영문대소문자, 한글을 제외한 나머지 지우기
    img_src = img['src'] # 웹툰 이미지의 링크
    print(title,img_src)
    urlretrieve(img_src, 'image/'+title+'.jpg') # image/참교육.jpg



img_one = img_tag[0]
print(img_one['title'])
print(img_one['src'])



















