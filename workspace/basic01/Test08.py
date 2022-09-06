'''
제어문
    조건문 : if
    반복문 : for while
    보조 제어문 : continue break

    for 변수 in 문자열|리스트|튜플:
        실행문들....

    for 변수 in range():
        실행문들....
'''
for i in "hello":
    print(i)

lst = [10,20,30,40]
for i in lst:
    print(i)

print("="*30)
for i in range(5): # (end) 0 ~ 4 (end 이전까지)
    print(i)

print("="*30)
for i in range(10,15): # (start,end) end 이전까지
    print(i)

print("="*30)
for i in range(10,-1,-2): #(start, end , step) start부터 end 이전까지 step씩 증감
    print(i)

# 구구단 3단 출력
for i in range(1,10):
    print("3 X",i,"=",3*i)
# 구구단 전체 출력
for i in range(1,10):
    for j in range(1, 10):
        print(i,"x",j,"=",j * i,end='  ')
    print("\n"+"="*120)
