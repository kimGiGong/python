'''
카톡 워드 클라우드
'''
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter

chat = ''
with open('KakaoTalk_20220908_1118_39_545_group.txt','r',encoding='utf-8') as txt:
    lines = txt.readlines()
    for l in lines:
        # print( l [ l.rfind( ']' )+1 : ])
        chat += l[l.rfind(']')+1:]

print(chat)

import re

chatRe = re.sub('[-=+,#@/\?:^$.*\"!~&%\\|\)\(\[\]\<\>`\']', '', chat)   # 특수 문자 제거
print(chatRe)
chatRe = re.sub('[0-9]','',chatRe)  # 숫자 제거
print(chatRe)
chatRe = re.sub('[A-Za-z]', '', chatRe)
print(chatRe)
chatRe = re.sub('이모티콘', '', chatRe)
chatRe = re.sub('년 월 일', '', chatRe)
print(chatRe)
chatRe = chatRe.replace('이모티콘\n','').replace('사진\n','').replace('\n\n','').replace('\\\\','')
chatRe = chatRe.replace('\t','')
print("*"*100)
print(chatRe)


# 명사만 추출
okt = Okt()
noun = okt.nouns(chatRe)
print(noun)


# 한글자 명사 삭제
for i, v in enumerate(noun):
    if len(v)<2:
        noun.pop(i)
print(noun)


# 명사 빈도 카운트
count = Counter(noun)
noun_list = count.most_common(10)
print(noun_list)

# # 워드 클라우드로 띄우기
# wc = WordCloud(font_path='C:\\Users\\tjoeun\\AppData\\Local\\Microsoft\\Windows\\Fonts\\D2Coding-Ver1.3.2-20180524-all.ttc'
#                , background_color='white', width=1000,height=1000,max_words=300
#                , max_font_size=300, colormap="PiYG")
#
# wc.generate_from_frequencies(dict(noun_list))
# wc.to_file('wordcloud_kakaoTalk.png')


# 마스크 씌우기
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

mask = Image.open('cloud.png')
mask = np.array(mask)
print(mask)


wc = WordCloud(font_path='C:\\Users\\tjoeun\\AppData\\Local\\Microsoft\\Windows\\Fonts\\D2Coding-Ver1.3.2-20180524-all.ttc'
               , background_color='white', width=1000,height=1000,max_words=300
               , mask=mask
               , max_font_size=300)
wc.generate_from_frequencies(dict(noun_list))
wc.to_file('wordcloud_kakaoMasking.png') # 파일로 저장
# 화면에 띄우기
plt.figure()
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()







