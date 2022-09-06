'''
예상할 수 없는 함수 : 매개변수에 전달되는 인자가 여러개일 경우 한곳에 받아 줄 수 있는 기능
def 함수명(*파라미터): * agrs
    실행문들...
'''

def sum(*num):
    tot = 0
    print(type(num))
    for i in num:
        tot += i
    return tot

print(sum(10,20,30,40,50))

print("hello", "hahaha")

print("*"*100)
def calc(oper, *num, test="hahaha"):
    if oper == 'sum':
        tot = 0
        for i in num :
            tot += i
    elif oper == 'mul':
        tot = 1
        for i in num:
            tot *= i
    print(tot)
    print(test)
    return tot

result = calc("sum",10,20,30,40,50, test = "kaka")
print(result)