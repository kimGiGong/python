# 네이버 영화 리뷰
import time

import requests
from bs4 import BeautifulSoup

headers = {"user-agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
for j in range(1, 6):
    url = 'https://movie.naver.com/movie/point/af/list.naver?&page=' + str(j)
    response = requests.get(url, headers=headers)
    # print(response)

    soup = BeautifulSoup(response.content, 'lxml')
    time.sleep(1)
    '''
    영화 제목
    #old_content > table > tbody > tr:nth-child(1) > td.title > a.movie.color_b
    #old_content > table > tbody > tr:nth-child(2) > td.title > a.movie.color_b
    #old_content > table > tbody > tr:nth-child(10) > td.title > 
    
    영화 평점
    #old_content > table > tbody > tr:nth-child(1) > td.title > div > em
    #old_content > table > tbody > tr:nth-child(2) > td.title > div > em
    #old_content > table > tbody > tr:nth-child(9) > td.title > div > em
    
    영화 평
    #old_content > table > tbody > tr:nth-child(1) > td.title
    #old_content > table > tbody > tr:nth-child(2) > td.title
    '''
    names = soup.select('a.movie.color_b') # 영화 제목
    stars = soup.select('td.title > div > em') # 영화 평점
    review_br = soup.select('td.title > br')
    # print(review)
    # print(len(review))
    print("name :",names[0].text)
    print("star :",stars[0].text)
    print("review :",review_br[0].next_element)
    for i in range(10):
        print("[", (i+1), "]영화 제목 :", names[i].text, ", 평점 :",stars[0].text)
        print("   리뷰 :", (review_br[i].next_sibling).__str__().strip()) # __str__() 문자열로 형변환
    print("=*"*25, j , 'page')












