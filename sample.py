#!user/bin/python
import sys

'''
print("===============")
print("test")
for i, value in enumerate(sys.argv):
    print(('argv[%d]:%s')%(i,value))

#os.listdir()을 사용해 폴더 내부의 파일명을 받아옵니다.
import os
folder_path = "경로"
floder_list = os.listdir(folder_path)
print(floder_list)

#폴더 한개에 대해 이름 변경하기
old_name = "C:/Users/wing7/Desktop/test_project/test_python/sample/꼬리치레"
new_name = "C:/Users/wing7/Desktop/test_project/test_python/sample/new_name"
os.rename(old_name, new_name)
'''

#여러 폴더에 대해 이름 변경하기
import os 

folder_path = "경로"

folder_list = os.listdir(folder_path)

for folder_name in folder_list :
    file_path = folder_path + "\\" + folder_name

    file_list = os.listdir(file_path)

    print("---------------------")
    print(folder_name+" have "+ str(len(file_list))+" files ")
    print("file_path : " + file_path)

    count = 1

    for file_name in file_list :
        old_name = file_path + "\\" + file_name
        new_name = file_path + "\\" + str(count) + ".jpg"

        try :
            os.rename(old_name, new_name)
            print("success : "+ file_name + " => "+ str(count)+".jpg")
        except:
            print("fail : "+ file_name + " => "+ str(count)+".jpg")
            print("------files already renamed number to new_name---------")
            break
            
        count = count +1

