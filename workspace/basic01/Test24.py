'''
with 키워드 이용해서 context manager 만들기

'''
with open("database.txt",'w') as file:  # file 에 저장이 됨
    file.write("아?\n")
    file.write("호우!\n")
    # file.close() : with open은 블럭이 끝나면 file이 없어지니 close도 필요없음


with open("database.txt",'r') as readfile:
    result = readfile.readlines()   # 파일 전체 읽어오기 -> 모든 줄을 리스트에 담아 리턴
    for r in result:
        print(r,end="")
    print(result)



























