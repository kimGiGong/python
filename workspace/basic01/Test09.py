'''
    3) 군집자료형
        문자열형      str       : " "
        리스트        list      : []
        튜플          tuple     : (,)
        딕셔너리      dict      : {:}
        집합          set       : {}

 * 튜플 tuple *
        리스트와 유사하나 수정 불가능한 점이 다르다. immutable
        구분 기호 : (,)
        데이터가 한개 저장하면 생성할때는 (,) 쉼표 반드시 기술
'''

t1 = () # 빈 튜플
t2 = tuple()
print(t1)
print(type(t2))

# 한개 요소만 대입시 쉼표 구분자
t1 = (10,)
print(t1)
print(type(t1))

# 요소가 두개 이상일 경우 소괄호 생략 가능
t1 = 10,20,30
print(t1)
print(type(t1))

# 수정 불가능
print(t1[0])
print(t1[1])
print(t1[2])
# t1[0] = 100
print(t1)

# 튜플 안에 요소가 mutable (수정가능) 타입이면 수정가능
t1 = (1,2,3,4,5,[10,20,30])
# t1[-1] = 111 # 튜플의 요소는 수정 불가능 -> 리스트 전체를 다른것으로 수정 불가능
t1[-1][1] = 3000  # 튜플 안의 리스트의 요소는 수정가능
print(t1)

# 튜플의 unpacking
tup = ("피카츄",20,"서울")
name, age , city = tup
print(name)
print(age)
print(city)

# 값교환
print("=="*10)
a,b = 10,20
a,b = b,a
print(a,b)

# 튜플 결합 : +
t1 = 1,2,3
t2 = "a","b","c"
t3 = t1 + t2
print(t3)

# 튜플 요소 할당 : *
t2 = t1*3
print(t2)

# in 연산자 not in
t1 = 1,2,"a","b"
print('a' in t1)

tList = [('피카츄',100),("라이츄",90),("꼬북이",75)]
for (i,j)in tList:
    print(i,"님의 점수는",j,"점 입니다.")

lst = [[1,2],[3,4],[5,6]]
for i,j in lst:
    print(i,"=",j)

# 내장 함수
tup = 1,2,3,4,5
#sum() 요소값 모두 하기
print(sum(tup))
#len() 요소의 갯수
print(len(tup))
#max(),min() 최대값 최소값
print(max(tup))
print(min(tup))
# index() 요소의 인덱스 값
print(tup.index(3)) # 3의 인덱스값 2


print("================================")
# count() 요소의 갯수 구하기
tup = 1,1,1,2,2,3
print(tup.count(3))























