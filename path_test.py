
import sys
print(sys.path)
print("_________________________")

import os
print(os.getcwd())
# 현재 디렉토리 위치 확인
print("_________________________")

print(os.system("dir"))
# dir이라는 OS 명령어 결과값 확인
print("_________________________")

f = os.popen("dir")
print(f.read())
print("_________________________")

import glob
input_dir = 'C:/Users/wing7/Desktop/aligned'
os.chdir(input_dir)
print(os.getcwd())
print("_________________________")
print(os.listdir(input_dir))
print(glob.glob("*"))
print("_________________________")

input_dir = 'C:/Users/wing7/Desktop/aligned'
file_list = os.listdir(input_dir)
print(file_list)

import os
import shutil

os.getcwd()
input_dir = 'C:/Users/wing7/Desktop/yolo-test/darkflow'
print(input_dir)

# 디렉토리명만 얻기
print(os.path.dirname(input_dir))
print("_________________________")

# 파일명만 얻기
if os.path.isfile(input_dir):
    print(os.path.basename(input_dir))
print("_________________________")

# 디렉토리명과 파일명을 나누어 얻기
dir, file = os.path.split(input_dir)
print(dir)
print(file)

print("_________________________")
print(os.listdir)


import os.path
targetdir = r"C:\Users\wing7\Desktop\aligned"
files = os.listdir(targetdir)

# file:17165.jpg 이런식으로 출력
for i in files:
    if os.path.isdir(targetdir+r"\\"+i):
        print("folder:"+i)
    else:
        print("file:"+i)


# file name :52196 이런식으로 출력
for i in files:
    if os.path.isdir(targetdir+"\\"+i):
        pass
    else:
        #print("file:"+i)
        if i.count(".") == 1 : #.이 한개일 때
            V = i.split(".")
            print("file name :"+V[0])
        else:
            print(len(i))
            for k in range(len(i)-1,0,-1): #.이 여러개일 때
                if i[k] == ".":
                    print("file name"+i[:k])
                    break
