# pandas

import pandas as pd
data1 = ['a','b','c','d','e']
print(data1)
print(type(data1))


print("+--+--++-+-+-+-+-+-+-+-+-+-")

# 1차원 Series 생성
sr1 =pd.Series(data1)
print(sr1)              # 문자열은 Object 로 나옴

print("+--+--++-+-+-+-+-+-+-+-+-+-")

sr2 = pd.Series(data=[11,22,33,44], index=['a','b','c','d'])
print(sr2)

print("+--+--++-+-+-+-+-+-+-+-+-+-")

# 인덱싱
print(sr2['a'])
print(sr2[2:4])
# [[]] 안에 인덱스 값을 넣어주면 행에 접근 가능
print(sr2[['a','c']]) # a,c 인덱스 두개 가져오기
# 슬라이싱
print(sr2['a':'c']) # c 포함 pandas 슬라이싱 이라서
print(sr2.index)    # index만 가져오기
print(sr2.dtype)
print(sr2.values)

print("+--+--++-+-+-+-+-+-+-+-+-+-")

# 연산
print(sr2)
print(sr2 * 2)

print("+--+--++-+-+-+-+-+-+-+-+-+-")

sr3 = pd.Series(data=[11,22,33,44], index=['a','b','d','e'])
print(sr2)
print(sr3)

print(sr2 + sr3) # NaN = Not a Number

print(sr2.sum())
print(sr2.mean()) # 평균
print(sr2.median())
print(sr2.max())
print(sr2.sort_values)
print(sr2.sort_index)

print("+--+--++-+-+-+-+-+-+-+-+-+-")

print(sr2.loc['a'])
print(sr2.loc['a':'c'])

















