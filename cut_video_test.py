import os
import glob

def menu():
    lof = glob.glob("*.mp4")

    for f in lof :
        print(lof.index(f)+1, f)

    nof = int(input("Number of file : "))
    name = lof[nof-1]    
    print(name)
    return name, name[:-4] + "_cut.mp4"

name, name2 = menu()
start = input("Start : ")
end = input("End : ")

command = f"ffmpeg -i {name} -ss {start} -to {end} -c:v copy -c:a copy {name2}"

os.system(command)