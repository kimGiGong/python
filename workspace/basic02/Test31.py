import numpy as np
arr = np.arange(10)
print(arr)
print(arr[3]) # indexing
print(arr[2:5]) # slicing
arr[2:5] = 15
print(arr)
print(arr[3:])
print(arr[:])

print("=====================================")
# 다차원
arr2d = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])
print(arr2d)
print(arr2d[2,1]) # add2d[행,열]
print(arr2d[[2,1],[3,3]]) # [행1,행2],[열1,열2]

print("*-*-*-*-*-*-*-*-*-*-*-*")
# 슬라이싱 [행:슬라이싱, 열:슬라이싱]
print(arr2d[2, : ])
print(arr2d[: ,1:3])
print(arr2d[:2 , 1:3])
arr2d[:2,1:3] = 0
print(arr2d)

print("=",50)

names = np.array(["AA","BB","CC","DD","EE"])
print(names)
print(names == "AA")

data = np.random.rand(5,3)
print(data)
print("======================================")
# 인덱싱 (행,열)
print(data[names=="AA",:])  # 인덱스 번호로 사용가능
print(data[(names=="AA") | (names=="D") ,: ])
print()

print(data)
print(data[:,1] > 0.5 )

print("======================================")
data[data[:,1] > 0.5 , 1] =1
print(data)

















