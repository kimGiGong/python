'''
 * 문자열 str *
    "문자열" '문자열' """ 여러줄 문자열 """(홑따옴표도 가능)

    1) 인덱스
        0 ~ 시작하는 인덱스 번호

    2) 인덱싱
    3) 특징
        수정 불가능함 immutable

    4) 슬라이싱
        문자열[시작인덱스:끝인덱스번호]


'''
str1 =""".?
안녕
어... 안녕"""
str2 = "hello"
str3 = "hello3"
print(str2[-2]) # 뒤에서 부터
print(str2[-1])
print(str2[0])
print(str2[1])
print(str2[2])
print(str3[0:2])
print(str3[:2])
print(str3[2:5])
print(str3[:])

str4 = "TheJoeun Institute"
# TheJoeun 만 출력
print(str4[0:8])
# Institute 만 출력
print(str4[-9:])
str5 = "prigraming"
print(str5[:2]+"o"+str5[3:6]+"m"+str5[-4:])
# programming으로 변경해서 출력

# 날짜 잘라보기
import datetime
today = datetime.date.today()
print(today)
print(type(today))

today = str(today)
print(today[:4])

# 문자열 관련 함수
str6 = "hello python"
print(str6)
str6 = str6.replace("python","pyCharm")
print(str6)

# split : 문자열 나누기
result = str6.split()   # 공백 기준으로 나누기
print(result)
result = "hello: hahaha".split(":")
print(result)

# 문자열의 길이 len()
str7 = "gsdgmskgsdfklghsfgshs"

# 문자열에 포함된 문자의 갯수 .count()
print(len(str7))
print(str7.count("F"))
print(str7.count("f"))  # 대소문자 구분

# find()  문자 인덱스 알아내기
name = 'thejoeun'
print(name.find('e'))
print(name.find('z'))   # 없는 문자는 -1 return
# index()  문자 인덱스 알아내기
print(name.index('j'))
#print(name.index('z'))  # 에러 발생


# 소문자 / 대문자로 리턴 lower()/ upper()
str8 = "Apple Tree"
print(str8.lower())
print(str8.upper())

# 공백 지우기 : strip(), lstrip(), rstrip()
str9 = "              python         "
print(str9.strip())     #       앞뒤 공백 제거
print(str9.lstrip())    # left  앞공백 제거
print(str9.rstrip())    # right 뒷공백 제거

