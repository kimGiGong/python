# 네이버 영화 랭킹 가져오기
import time

import requests
from bs4 import BeautifulSoup

'''
<tr>		
    <td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r01.gif" alt="01" width="14" height="13"></td>

    <td class="title">
        <div class="tit5">
            <a href="/movie/bi/mi/basic.naver?code=213364" title="인생은 뷰티풀: 비타돌체">인생은 뷰티풀: 비타돌체</a>
        </div>
    </td>
    <!-- 평점순일 때 평점 추가하기  -->

    <td>
        <div class="point_type_2">
            <div class="mask" style="width:98.4000015258789%">
                <img src="https://ssl.pstatic.net/imgmovie/2007/img/common/point_type_2_bg_on.gif" width="79" height="14" alt="">
            </div>
        </div>
    </td>
    <td class="point">9.84</td>
    <td class="ac">
        <a href="/movie/point/af/list.naver?st=mcode&amp;sword=213364" class="txt_link">평점주기</a>
    </td>

    <!----------------------------------------->  
    <td colspan="2" class="new_icon">
      <img width="20" height="5" alt="new" src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_new_1.gif">
    </td>

</tr>
'''


'''
<tr>

    <td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r02.gif" alt="02" width="14" height="13"></td>
    <td class="title">
        <div class="tit5">
            <a href="/movie/bi/mi/basic.naver?code=81888" title="탑건: 매버릭">탑건: 매버릭</a>
        </div>
    </td>
    <!-- 평점순일 때 평점 추가하기  -->

    <td><div class="point_type_2"><div class="mask" style="width:97.70000457763672%"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/point_type_2_bg_on.gif" width="79" height="14" alt=""></div></div></td>
    <td class="point">9.77</td>
    <td class="ac"><a href="/movie/point/af/list.naver?st=mcode&amp;sword=81888" class="txt_link">평점주기</a></td>

<!----------------------------------------->  

    <td class="ac">
        <img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10" class="arrow">
    </td>
    <td class="range ac">1</td>
</tr>
'''

'''
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(3) > td.title > div > a
#old_content > table > tbody > tr:nth-child(4) > td.title > div > a


#old_content > table > tbody > tr:nth-child(2) > td.point
#old_content > table > tbody > tr:nth-child(3) > td.point
#old_content > table > tbody > tr:nth-child(4) > td.point

'''

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220912"
headers = {"user-agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
# print(res)
soup = BeautifulSoup(res.content,'lxml')
# print(soup)
# mv_name = soup.find_all('td',class_="tit5")
mv_name = soup.select("div.tit5 > a")
mv_star = soup.select('td.point')
for i in range(50):
    print("영화 :",mv_name[i].text," = ", mv_star[i].text)
# print(mv_name)
time.sleep(1) # 1초 실행 정지