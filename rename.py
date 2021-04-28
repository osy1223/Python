import os
import shutil

input_dir = '경로'  
save_dir = '경로' 
a = 0
os.chdir(input_dir) # os.chdir : 디렉토리 변경하기
print('Load File : ', os.getcwd()) # os.getcwd() : 현재 디렉토리 확인(=현재 작업 폴더 열기)
print('Save File : ', os.path.abspath(save_dir)) # os.path.abspath : 특정 경로에 대해 절대 경로 얻기

if os.path.isfile(os.path.join(save_dir, "00001.jpg")): # os.path.isfile : 경로 중 파일명만 얻기
    a = len(os.listdir(save_dir)) # os.listdir() : 경로를 입력하면 경로 안의 파일 목록을 리스트로 반환
    print('There are already {} files'.format(a))

for i, file in enumerate(os.listdir()): # os.listdir() : 디렉토리 안의 파일/서브 디렉토리 리스트
    rename = '{0:05d}'.format(i+1+a) + '.jpg'
    print(rename)
    shutil.copyfile(os.path.join(input_dir, file), os.path.join(save_dir, rename)) 
    # shutil.copyfile(원본 파일 경로, 대상 파일 경로) : 원본이 파일이 아니라 폴더이면 에러 발생
    # os.path.join : 경로를 병합하여 새 경로 생성
    