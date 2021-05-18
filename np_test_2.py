import numpy as np

# 10.Masking연산 

# boolean 조건 배열을 이용해서 원하는 위치의 요소값만 변경
a = np.arange(0,16)
b = a.reshape(4,4)
c = b>8
b[c] = 0

# print(c)
#print(b)

# 11. 배열 요소의 최대, 최소, 합, 평균 구하기
a = np.arange(0,16).reshape(4,4)

#max = np.max(a)

# 축(axis에 대한 연산)
max = np.max(a, axis=0)
min = np.min(a, axis=0)
sum = np.sum(a, axis=0)
mean = np.mean(a, axis=0)
'''
print(max)
print(min)
print(sum)
print(mean)
'''
# 12. 주어진 범위에서 일정한 간격으로 배열 만들기
# 0~19까지 3개의 요소로 구성된 배열을 생성
a = np.linspace(0,10,3)
#print(a)

'''
# 13. 중복되는 요소 제거
a = np.array([1,2,2,2,3,4,2,5,6,7,9])
b = np.unique(a)
#print(b)

# 14. 인덱스 리스트를 통한 특정 원소 값 얻기
matrix = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
#(0,1)과 (2,0)의 위치에 대한 값을 출력
#print(matrix[[0,2],[1,0]])

# 15. 다차원 배열을 1차원 배열로 만들기 지원하는 함수 3개
# ravel(), reshape(), flatten()

# 16. 전치행렬 및 행렬식 구하기
a = np.array([
    [1,2,3],
    [2,4,6],
    [3,8,9]
])
#linalg = 행렬식(역행렬이 존재하는지 여부를 확인하는 방법)
#print(np.linalg.det(a))
#print(a.T)

# 17. 대각행렬을 뽑아내거나, 대각 행렬 만들기
#print(a.diagonal(offset=0))
#offset은 기본값이 0, 이 값을 조정하여 뽑아낼 대각성분의 위치를 조정할 수 있다.
#print(np.diag(a))
# diagonal = np.diag(a) 동일한 기능

# 18. 인덱스값을 담은 배열로 다른 배열의 요소값 뽑아내기
W = np.arange(21).reshape(7,3)
#print(W)

idx = np.array([1,0])
#print(W[idx])

# 19. 배열의 요소값 이산화
#a = np.array([1,2,3,4,5,6,7,8])
#b = np.digitize(a, bins=[3,6])
#c = np.digitize(a, bins=[3,6], right=True)
#print(c)
#[최소,3),[3,6),[6,최대] 구간에 포함되는 요소를 각각 0,1,2로 이산화

# 20. 배열 요소 전체에 대한 지정 표현
a = np.empty((3,3,3))
print('a=',a)
print('a[...]=', a[...])
print('a[0,...]=',a[0,...])
print('a[0,0,...]=',a[0,0,...])
print('a[0,0,0]=',a[0,0,0])
'''

# 21. NaN값 삭제하기
a = np.array([
    [1,2],
    [3,4],
    [np.nan,4],
    [2,np.nan],
    [4,5]
])

b = a[~np.isnan(a).any(axis=1)]
#print(b)

# 22. 특정한 값 대체하기 
X = np.array([
    [0,1,1],
    [1,2,3],
    [2,3,5],
    [3,2,1],
    [4,1,6]
])

# 배열 요소 중에 2인 항목을 100으로 변경하고자 할때 
X = np.where(X==2, 100, X)
#print(X)

# 23. 두 배열 합치기
X = np.array([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])
Y = np.array([
        [100, 101, 102],
        [103, 104, 105],
        [106, 107, 108]
    ])
# vstack : 수직방향으로 합치기
V = np.vstack((X,Y))
#print(V)
# hstack : 수평방향으로 합치기
H = np.hstack((X,Y))
#print(H)
# concatenate : 합치고자 하는 배열에 맞게 합치는 것
C = np.concatenate((Y,X))
#print(C)

X = np.array([0,1,2])
Y = np.array([100,101,102])
C = np.concatenate((X, Y))
print(C)
X = np.array([[0],[1],[2]])
Y = np.array([[100],[101],[102]])
C = np.concatenate((X, Y))
print(C)