'''
* 예외 처리 exception handler *
    에러의 예
        IOError
        IndexError
        ImportError
        ValueError
        ZeroDivisionError
        FileNotFoundError
        SyntaxError
        EOFError

    예외 처리 구문
        try:
            에러 발생할 수 있는 코드들
        except 발생 에러 as 에러메세지담을변수:
            에러 발생시  처리할 코드들

'''
print("프로그램 시작!!")
YN = input("Y N")
if YN == "Y":
    YN = True
else:
    YN = False
while YN:
    try:
        num = input("정수 : ")
        int(num)    # 에러 발생!
        print(num)
        if int(num) == 0 : break
    except ValueError as e:
        print("값이 이상해요!! 에러 발생!!",e)
    finally:
        print("예외 발생 여부와 상관없이 무조건 실행되는 블럭!")
print("프로그램 종료!!")


def func():
    try:
        num = int(input("1~5 사이 정수를 입력 :"))
        if num > 5 or num < 1:
            print("잘못 입력")
            raise  # 강제로 예외 발생
    except ValueError:
        print("내부에서 바로 잡자")
    else:
        print("입력값 : ",num)


try:
    func()
except RuntimeError:
    print("예외 잡자~~~")


num = [1,2,3,4]
result = [a * 3 for a in num]
print(result)