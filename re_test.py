import os
import shutil


input_dir = 'C:/Users/wing7/Desktop/fetch_0531_total/rui_xseg'  
save_dir = 'C:/Users/wing7/Desktop/0603+rui' 

folder_name = os.path.basename(input_dir)
# print("a : ",a) 폴더명
file_name = os.listdir(input_dir)
# print("b :", b) 파일명

if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

for i in range(len(file_name)):
    name = file_name[i]
    print(name)
    rename = (folder_name+'_'+name) # 폴더명_파일명으로 rename
    print(rename)
    print('{}===============>{}'.format(name, rename))
    shutil.copyfile(os.path.join(input_dir, name), os.path.join(save_dir, rename))

'''
for i, file in enumerate(os.listdir()): 
    #rename = str(input_dir)+'_'+ str(file)
    #rename = input_dir.replace("/", "").replace(":","") + '_' + str(file)
    #print("현재경로:",os.getcwd())
    #rename = a +'_'+ str(file)
    print('{} =======> {}'.format(file,rename))

    #print("input_dir, file :"+os.path.join(input_dir, file))
    #print("save_dir, rename : "+os.path.join(save_dir, rename))
    shutil.copyfile(os.path.join(input_dir, file), os.path.join(save_dir , rename))
    # shutil.copyfile(원본 파일 경로, 대상 파일 경로) : 원본이 파일이 아니라 폴더이면 에러 발생
    # os.path.join : 경로를 병합하여 새 경로 생성
'''