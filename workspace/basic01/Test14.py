'''
## 문제 : 성적 처리 프로그램
아래 메뉴를 출력하고, 원하는 서비스 번호를 입력 받아 진행되는
프로그램을 만들어 보세요.


*** 저 조은 LMS ***
1. 학생 정보 출력
2. 학생 정보 입력
3. 학생 정보 수정
4. 학생 정보 삭제
5. 학생 정보 검색
6. 전체 총점 , 평균 출력
7. 프로그램 종료

- 학생 정보는 dict 타입에 저장 : key = 학생이름 , value = 파이썬점수
- 각 메뉴에 해당하는 기능은 함수 들로 구성
    def = define (정의하다)


'''
student = {}
while True:

    msg ="잘못된입력"

    def menu (inputnum):
        if int(inputnum) == 1:
            read(student)
        elif int(inputnum) == 2:
            add()
        elif int(inputnum) == 3:
            modify(student)
        elif int(inputnum) == 4:
            remove(student)
        elif int(inputnum) == 5:
            search(student)
        elif int(inputnum) == 6:
            allscore(student)
        elif int(inputnum) == 7:
            print("종료")
        else: print(msg)





    def read (student):
        for n,s in student.items():
            print("학생이름",n,",점수",s)

    def add ():
        name = input("추가 할 학생이름 ")
        score = int(input("점수 "))
        student.update({name:score})


    def modify (student):
        name = input("수정 할 학생이름 ")
        if student.keys().__contains__(name) :
            for n,s in student.items():
                if n.__contains__(name):
                    score = input("점수 입력>>")
                    student.update({name: score})
        else:
            print("존재 하지 않는 학생")


    def remove (student):
        name = input("삭제 할 학생이름 ")
        if student.keys().__contains__(name) :
            for n, s in student.items():
                if n.__contains__(name):
                    student.__delitem__(name)
                    break
        else:
            print("존재 하지 않는 학생")


    def search (student):
        name = input("찾을 학생이름")
        if student.keys().__contains__(name) :
            for n, s in student.items():
                if n.__contains__(name):
                    print("학생이름", n, "점수", s)
                    break
        else:
            print("존재 하지 않는 학생")


    def allscore (student):
        tot = sum(student.values())
        size = len(student.values())
        print("총점",tot)
        print("평점",tot/size)









    print("""*** 저 조은 LMS ***
    1. 학생 정보 출력
    2. 학생 정보 입력
    3. 학생 정보 수정
    4. 학생 정보 삭제
    5. 학생 정보 검색
    6. 전체 총점 , 평균 출력
    7. 프로그램 종료""")
    inputnum = input("입력 >>")



    menu(inputnum)
    if int(inputnum) == 7:
        break


