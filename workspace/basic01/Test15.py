# ** 별 두개는 키,밸류 형태의 값을 여러개 받을수 있다.
def packer(name=None ,**kwargs):
    print(name)
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    for i,j in kwargs.items():
        print("{}:{}".format(i,j))

packer(age="30",mobile="010-1111-2222",city="Seoul")

#dict unpacking
def unpacker(name=None ,score=None):
    if name and score:  # 둘중 하나라도 값이 없으면 False
        print("안녕하세요,{}님의 점수는 {} 점 입니다.".format(name,score))

    else:
        print("이름이나 점수가 없네요~~ 잘좀하지...")

unpacker(**{"name":"김피카","score":100}) # dict를 서치해서 매개변수에 넣는다

















