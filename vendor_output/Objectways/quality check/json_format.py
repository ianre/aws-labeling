import os
import shutil
import json


src = os.path.dirname(os.path.realpath(__file__))
src = os.path.join(src, "images","vir_edu")
folders = os.listdir(src)
dest = os.path.dirname(os.path.realpath(__file__))
count = 0
json_location = os.path.join(dest, "instances_default.json")

print("json_location",json_location)

with open(json_location) as f:
    data = json.load(f)
  #print(data["images"])


for annotation in data['annotations']:
    c_id =  annotation['category_id']
    if c_id==1:
        annotation['category_id'] = 302802
    elif c_id==2:
        annotation['category_id'] = 302803
    elif c_id==3:
        annotation['category_id'] = 302804
    elif c_id==4:
        annotation['category_id'] = 302805
    count+=1
    annotation['id'] = count
        

'''
for image in data['images']:
    
    filename = image['file_name']
    from_video = filename.split('/')[1][:-4]
    frame = filename.split('/')[2]

    image_loc = os.path.join('',from_video + '_' + frame)
    print("image_loc:",image_loc)
    image['file_name'] = str(image_loc)
    print(image['file_name'])
    count+=1
'''

with open(json_location, "w") as jsonFile:
    json.dump(data, jsonFile)

#print(os.listdir(dest))
print(count)


