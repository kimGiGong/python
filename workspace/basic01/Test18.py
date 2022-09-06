# 상속
class Student1 :
    def python(self):
        print("재밌는 파이썬!!!")


class Student2:
    def c(self):
        print("지루한 C언어....")

class Student3:
    def java(self):
        print("자바는 이제 그만~")


# 상속 받는 클래스

class Pika (Student1,Student2,Student3):
    pass


pikapika = Pika()
pikapika.java()


class Person:
    __juminNum = "1010011-1010101"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(Person.__juminNum)
        print("부모생성자")

    def show(self):
        print("부모")
        print("이름 : ",self.name)
        print("나이 : ",self.age)

# ----------------------------------
class Student(Person):



    #  오버라이딩
    def __init__(self,name,age,hakbun):
        super().__init__(name,age)  # 부모생성자 호출
        self.hakbun = hakbun

        print("자식 생성자")

    def show(self):
        print("자식")
        super().show()
        print("학번 : ", self.hakbun)
# ----------------------------------------------

pk = Student("피카츄",20,2022)
pk.show()

print(Person._Person__juminNum) # 숨긴 변수 표기





















