'''
* 생성자 init 메서드

'''
class Person:
    # 클래스 변수
#    name = ""   # 클래스 변수
#    age = 0
    def __init__(self,name,age):
        #인스턴스 변수
        self.name = name
        self.age = age
        print("생성자 호출!")
#---------------------------------
ps = Person("라이추",10)
print(ps.name)
print(ps.age)
#print(Person.name)  # 인스턴스 변수를 초기화 시켜준 것
#print(Person.age)   # 클래스 변수를 초기화 시켜준것이 아님
# 따라서 클래스 변수가 필요하지 않다


class Npc:
    # 클래스 변수 생성
    count = 0 # Npc가 만들어질 때마다 Npc의 수를 카운팅할 변수 (공용)

    def __init__(self,name):
        self.name = name    # 인스턴스 변수 생성
        print("{} 만들어지는 중....".format(self.name))
        Npc.count += 1


    def die(self):
        print("{}가 죽었습니다.....ㅠㅠ".format(self.name))
        Npc.count -= 1


    def showInfo(self):
        print("생존하고 있는 NPC는 {}명 입니다".format(Npc.count))

# -------------------------------- 클래스 구분선 --------------

elf1 = Npc("엘프1")
elf2 = Npc("엘프2")
elf3 = Npc("엘프3")
elf1.showInfo()
elf2.die()
elf1.showInfo()
print("*=-"*50)

class Paymemt:
    # 클래스 변수
    count = 0       # 제품의 총 개수
    discount = 0.2  # 할인율

    # 생성자
    def __init__(self,price,number):
        # 인스턴스 변수
        self.price = price
        self.number = number
        Paymemt.count += 1

    # 인스턴스 메서드
    def calulator(self):
        #인스턴스 변수
        self.pay = self.price * self.number # 정가
        self.dc_pay = self.pay - (self.pay * Paymemt.discount)  # 할인가

    # 인스턴스 메서드
    def display(self):
        print(Paymemt.count, "번째 제품입니다")
        print("정가 : ",self.price)
        print("수량 : ",self.number)
        print("가격 : ",self.pay)
        print("할인가 : ",self.dc_pay)


    # 스태틱 메서드
    @staticmethod
    def welcome():  # self 자동생성 안됨 일반메서드 추가와 같다
        print("어서오세요~")
        print("할인중입니다.")

    # 클래스 메서드
    @classmethod
    def update(cls,value):
        # 할인율 조정 : 1 이상이거나 0이하면,
        # 할인융을 입력받도록
        while value >= 1 or value <= 0:
            value = float(input("할인율을 다시 입력하세요 : "))
        cls.discount = value



# ----------------------------------------------------------
p1 = Paymemt(1000,5)
p1.calulator()
p1.display()

Paymemt.update(1)


p2 = Paymemt(2000,4)
p2.calulator()
p2.display()
p2.welcome()


























