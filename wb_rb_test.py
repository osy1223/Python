import sys
import os
#print("sys.path: \n",sys.path)
#print("os.getcwd: \n",os.getcwd)

input_dir = 'C:/Users/wing7/Desktop/test_project/test_python/python_test/test.txt'

'''
f = open(input_dir, mode='rt', encoding='utf-8')
s1 = f.readline()
s2 = f.readline()
#print(s1)
#print(s2)
f.close()

try :
    f = open(input_dir, mode='rt', encoding='utf-8')
    for line in f:
        print(line)
finally:
    f.close()
'''
'''
# 텍스트 파일
with open(input_dir, mode='rt', encoding='utf-8') as f:
    for line in f:
        print(line)

#이미지 바이너리 파일로 읽어 한 바이트씩 프린트 하는 예제
test_img = 'C:/Users/wing7/Desktop/test_project/test_python/OpenCV/a.PNG'
with open(test_img, "rb") as f:
    byte = f.read(1)
    while byte != b"":
        print(byte)
        byte = f.read(1)
'''

# 바이너리 파일을 읽기 위해서는 파일모드를 rb로, 쓰기 위해서는 wb 로 지정
# 바이너리 쓰기
data = [1,2,3,4,5]
with open("test.bin", "wb") as f:
    f.write(bytes(data))

# 바이너리 읽기
with open("test.bin", "rb") as f:
    content = f.read()
    print(type(content))
    for b in content:
        print(b)
