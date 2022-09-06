'''
파라미터와 인자 : 개수, 순서가 일치 해야 한다.
파라미터의 초기값 지정.
초기값이 파라미터에 지정되어있으면, 인자를 생략 가능.
'''
from operator import ge


def func(username,password,name,gender,email,nation="S.Korea"): # nation 초기값 지정
    print(username)
    print(password)
    print(name)
    print(gender)
    print(email)
    print(nation)


func('피','카','김피카','츄','츄@츄')   # 6개 파라미터 지만 초기값 지정으로 5개 입력으로도 가능

'''
파라미터와 인자 : 개수, 순서가 일치 해야한다.
파라미터 순서 바꿔도 사용 가능한 방법
함수 호출 할때 인자 기입시, 파라미터명 = 값

'''
print("="*50)
func(name="피카츄",password="1234",email="니얼굴", gender="F",username="아", nation="오")


# 리턴
print("="*50)
def calc(num1 , num2):
    return num1+num2 , num1- num2

print(calc(10,20))
res1 , res2 = calc(100,400)
print(res1)
print(res2),











