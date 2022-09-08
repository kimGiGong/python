
'''
* 선형 회귀 linear regression *

    f(x) = ax + b



'''
import numpy as np
from sklearn.linear_model import LinearRegression  # 선형회귀 임포트
from matplotlib import pyplot as plt

# 배민 배달 속도 데이터
# [ 거리, 시간 ]
data = np.array([[100, 20],
                 [150, 24],
                 [300, 36],
                 [400, 47],
                 [130, 22],
                 [240, 32],
                 [350, 47],
                 [200, 42],
                 [100, 21],
                 [110, 21],
                 [190, 30],
                 [120, 25],
                 [130, 18],
                 [270, 38],
                 [255, 28]])

# 거리
print(data[:, 0])
# 시간
print(data[:, 1])

# 데이터 그래프에 점으로 뿌리기
# plt.scatter(data[:, 0], data[:, 1])
# plt.title("Time / Distance")        # 타이틀
# plt.xlabel("Distance(meter)")       # x축 라벨
# plt.ylabel("Time(mit)")             # y축 라벨
# plt.axis([0, 450, 0, 50])        # 그래프 축 사이즈 설정[ 가로 min, 가로 max , 세로 min , 세로 max ]
# plt.show()

# 선형 회귀 모델 적용
# LinearRegression : [ [data] , [data] , [data] ] 2차원 배열
print(data.shape)       # 15행 2열 (15,2)
print(data.shape[0])    # 행의 갯수 숫자 뽑기
'''
# test
test = np.array([1,2,3,4])
test2 = test.reshape(2,2) #(행갯수, 열갯수)
print(test)
print(test2)
'''
# 거리  [ 100 150 300 ... ] 1차원 배열 -> 행열인 2차원으로 변경 == 데이터개수만큼행, 1열
meter = data[:,0].reshape(data.shape[0],1)
print(meter)
# 시간 [ 20 24 36 ... ] 1차원 배열 -> 행열 = 데이터 갯수만큼, 1열
min = data[:,1].reshape(data.shape[0],1)
print(min)


# 선형회귀 객체 생성
model = LinearRegression()

# 학습 시키기 fit()
model.fit(X=meter, y=min)

# 예측하기 : predict(시험값)
print("500m일때 소요시간 예측치 :", round(model.predict([[500]])[0][0], 2), "분 예상" )

# 선 그리기
plt.grid(True)
plt.plot(meter, min, 'b.')
# plt.show()

# 예측할 거리(범위) 2차원 리스트로 작성
x_dis = [[0], [500]] # 선을 그려줄 시작과 끝 거리
plt.plot(x_dis, model.predict(x_dis), color="r")
plt.show()

















