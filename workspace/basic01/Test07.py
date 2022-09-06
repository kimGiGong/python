'''
 제어문
    조건문 : if
    반복문 : for while
    보조제어문 : continue, break

 * 반복문 while *
    while 조건식 :
        반복할 실행문들....

    while True :
        실행문들....
        if 조건식 : break  * 종료 시점 필요 *


'''

i = 0  # 초기식
while i < 10:  # 조건식
    print(i)
    i += 1  # 증감식

# 1 ~ 10 까지의 짝수를 모두 더한 값 출력
print("*" * 30)
sum = 0
i = 1
while i <= 10:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)

print("="*40)

while True:
    num = int(input("숫자입력 (9종료) : "))
    print(num)
    if num == 9:
        break
print("while True 종료")