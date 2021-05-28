
f = open("새파일.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다\n" % i
    f.write(data)
f.close()

f = open("C:/Users/wing7/Desktop/test_project/test_python/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line : break
    print(line)
f.close()


while 1:
    data = input()
    if not data: break
    print(data)


f = open("C:/Users/wing7/Desktop/test_project/test_python/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("C:/Users/wing7/Desktop/test_project/test_python/새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가
f = open("C:/Users/wing7/Desktop/test_project/test_python/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#with을 사용하면 자동으로 close
with open("C:/Users/wing7/Desktop/test_project/test_python/테스트.txt", "w") as f:
    f.write("Life is too short, you need python")

import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
