# 네이버 it 기사 헤드라인
import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
headers = {"user-agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
# 페이지 요청
res = requests.get(url, headers=headers)
# 파싱
soup = BeautifulSoup(res.content, 'lxml')
# print(res) # 200이뜨면 제대로 요청된거

ul_tag = soup.select('ul.type06_headline')
li = ul_tag[0].select('li')
for l in li:
    a = l.select('dl > dt:nth-child(2) > a')
    print(a[0].text.strip)
print(ul_tag)

a_tag = soup.select('ul.type06_headline > li > dl > dt:nth-child(2) > a')
print(len(a_tag))
# print(a_tag)
for a in a_tag:
    print(a.text.strip())

# CSS 셀렉터로 패턴 분석
# #main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a        # copy collector 로 복사하면 일케나옴
# #main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(2) > dl > dt:nth-child(2) > a
# #main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(3) > dl > dt:nth-child(2) > a














