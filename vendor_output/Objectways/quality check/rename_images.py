import os
import shutil


src = os.path.dirname(os.path.realpath(__file__))
src = os.path.join(src, "images","vir_edu")
folders = os.listdir(src)
dest = os.path.dirname(os.path.realpath(__file__))
count = 0

for folder in folders:
    #print(folder)
    folder_path = os.path.join(src, folder)
    images = os.listdir(folder_path)
    for image in images:
        #print(image)
        if os.path.isfile(os.path.join(folder_path,image)):
            full_file_name = os.path.join(folder_path,image)
            new_file_name = os.path.join(dest,folder[:-4]+"_"+image)
            print("Image found:",full_file_name, " going here: ",new_file_name)
            shutil.copy(full_file_name,new_file_name)
            count+=1

print("count",count)