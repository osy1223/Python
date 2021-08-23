import os
import shutil


input_dir = r'C:\Users\wing7\Desktop\dob_m_360_001\right_90_0@'  
input_dir = input_dir.replace('\\','/')
print(input_dir)
save_dir = r'C:\Users\wing7\Desktop\1' 
save_dir = save_dir.replace('\\','/')
print(save_dir)




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

