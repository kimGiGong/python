'''
* 연산자 operator *
    산술      + - * / %
    대입      =
    복합대입    += -= *= /= %=
    비교        > >= < <= == !=
    논리        or    and    not
    멤버        in / not in
    식별        is  /  is not

    증감 연산자는 X 없음
    ++ --
'''

num1 = 10
num2 = 3
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2) # 몫값만 필요할때 (정수 / 정수 = 정수)
print(num1 % num2)
print("*"*50)
print(num1 < num2)
print(num1 == num2)
print(num1 != num2)
print(num1 != num2 or num1 > 100)
print(not(num1 == num2))

print("*"*10+" list "+"*"*25)
lst = [1,2,3,4,5] # list list도 키워드
print(10 not in lst)
a=10
b=20
print( a is b)
print(id(a))
print(id(b))

