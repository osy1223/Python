import numpy as np

# 0.배열 생성
#a = np.empty([3,3])
#print(a)

#b = np.random.randn(3,3)
#print(b)

# 1.배열로 생성
#x = np.array([1.,2.,3.,4.])
#print(x)
#print(type(x))
#print(x.shape)
#print(np.ndim(x))

#y = np.array([[1.,2.,3.,4.],[9.,8.,7.,5.]])
#print(y.shape)
#print(np.ndim(y))

'''
# 2.원소의 접근
z = np.array([[1,2,3],[4,5,6]])
print(z[0])
print(z[0][0])
print(z[0][0]==z[0,0])

for r in z :
    print(r)
'''

'''
# 3.산술 연산
a = np.array([10,20,30])
b = np.array([1,2,3])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
'''

'''
a = np.arange(20).reshape(5,4)
b = np.arange(4)

#print(a)
#print(b)

# np.add.at(A, idx, B)는 B를 A의 idx 번째 행에 더하는 연산
np.add.at(a,1,b)
print(a)
'''

'''
# shape가 다른 배열 간에도 브로드캐스트 처리
a = np.array([[1,2],[3,4]])
b = np.array([[100],[200]])
c = np.array([[100,200]])

print("a+b: \n",a+b)
print("a+c: \n",a+c)
'''

'''
# 행렬의 곱(내적) 연산
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.dot(a,b)
print(c)
'''

'''
# 배열 요소의 합과 곱
a = np.array([1.,2.,3.])
print(np.sum(a))
print(np.prod(a))

# True = 1, False = 0 으로 변환되어 합산
z = np.array([True, False, True, False])
print(np.sum(z))
'''

'''
# 배열 요소 중 최대값의 인덱스 구하기
x = np.array([[0.1,0.8,0.1],
              [0.3,0.1,0.6],
              [0.2,0.5,0.3],
              [0.8,0.1,0.1]])
y = np.argmax(x)
y0 = np.argmax(x, axis=0)
y1 = np.argmax(x, axis=1)
#axis=0 : 세로방향(열) , axis=1 : 가로방향(행)
print(y)
print(y0)
print(y1)
'''

'''
# 배열 요소 중 임의로 몇개만 뽑아내기
a = [10,20,30,40,50,60,70,80,90]
n = np.array(a)
i = np.random.choice(n.shape[0], 3)
# 총 9개의 요소 중 3개의 요소를 임의로 뽑기
print(i)
s = n[i]
print(s)


# 요소를 선택하는 기준에 대해, 각 요소가 선택될 확률을 지정
n = np.array([10,20,30,40,50,60,70,80,90])
p = np.array([0,0,0,0,0,0,1,0,0])
i = np.random.choice(n.shape[0], 3, p=p)
# p에서 6번째 선택해서 n에서 6번째 값인 70 선택(1=선택확률100%,0=0%)
print(i)
s = n[i]
print(s)
'''

# 배열 요소의 형 변환
a = np.array([-1.0,1.0,2.0])
#b = a>0.0

# 배열을 생성할 때 타입을 강제로 지정도 가능
b = np.array(a > 0.0, dtype=np.int)
c = b.astype(np.int)

print(b)
print(c)

