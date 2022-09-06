from builtins import print



'''
# 1. 출력문
    print()
    * 연결하여 출력
    문자 + 문자 : 문자 연결 되어 출력
    문자 , 문자 : 띄어쓰기 되어 출력
    숫자 + 숫자 : 연산 결과 출력
    숫자 , 숫자 : 나란히 출력
    문자 , 숫자 : 나란히 출력
    문자 + 숫자 : 에러!!
    문자 * 숫자 : 문자가 숫자만큼 반복되어 출력

'''
print(10)
print("hello")
print('hello2')

#   print("10" + 10)    에러!
print("문자","문자2")
print(10,10)
print("hello " * 10)

print("엔터기능 없애기 ", end ="")
print("다음 줄에 출력??")
'''
* 이스케이프 문자
    \ n : 줄바꿈
    \ t : 탭간격
    \ ' : 홑따옴표 문자로 출력 
    \ " : 겹따옴표 문자로 출력 
    
'''
print("내 \t 이름은 \"피카츄\" 입니다.")

name = "잔망루피"
age = 10
print("내 이름은",name, "입니다")
# 서식문자 : 정수 %d , 실수 %f , 문자열 %s
print("내 이름은%s입니다. 나이는 %d 살 입니다" % (name, age))
# format
print("내이름 {} 아니다. 나이는 {} 살 이다." .format(name, age))


'''
 * 데이터 타입 (자료형) *
 
    1) 숫자형
        정수          int (python ver 3.x)  int,long(python ver 2.x)
        실수          float   (python 3.x) 5000/3 = 1666.66666
                              (python 2.x) 5000/3 = 1666
        
    2) 참/거짓형
        bool(boolean)   True / False
    
    3) 군집자료형
        문자열형      str       : ' '    " "
        리스트        list      :
        튜플          tuple
        딕셔너리      dict
        집합          set

 * 변수 variable *
    변수명 = 값   

    type (값/변수) : 데이터 타입 확인 가능
    
    변수명 규칙
        숫자로 시작X, 대소문자 구분 num Num
        특수기호  _ (밑줄)만 허용
        keyword 사용불가
        
'''
print("*"* 50)
num = 10
print(num)
print(type(num))
print(id(num))  # ref 주소값
num2 = 2.14
print(num2)

hello = "안녕하세요"
print(hello)

'''
* 입력문 * 
    변수 = input("콘솔에 띄울 메세지")
    input() : 콘솔을 통해서 값 입력. 문자열로 리턴
    
* 형변환 casting, convert *
    문자 ------> int
         int(값)
    문자 ------> float
        float(값)
    int , float -----> 문자
                str(값)
    
'''
print("*"*50)
msg = input("메세지 입력 >>")
print(msg)

age = int(input("나이입력"))
print(age-1)

