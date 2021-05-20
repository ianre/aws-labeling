import os
import shutil
import json
import numpy as np


src = os.path.dirname(os.path.realpath(__file__))
dest = os.path.dirname(os.path.realpath(__file__))
count = 1
json_location = os.path.join(dest, "instances_default.json")

print("json_location",json_location)

with open(json_location) as f:
    data = json.load(f)
  #print(data["images"])

'''
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
    json_annote = os.path.join(filename[:-4]+"json")
    #print(json_annote)
    with open(json_annote) as file:
        annotations = json.load(file)
    for annotation in annotations['annotations']:
        #print(annotation)
        c_id =  annotation['name']
        obj_id = 0
        if c_id=="Left-Grasper":
            obj_id = 302802
        elif c_id=="Right-Grasper":
            obj_id = 302803
        elif c_id=="Needle End":
            obj_id = 302804
        elif c_id=="Needle Tip":
            obj_id= 302805
        # add to this: data["annotations"]
        if c_id == "Left-Grasper" or c_id == "Right-Grasper":
            annote_string = []
            max_y = 0 
            max_x = 0
            min_x = 1000
            min_y = 1000 
            
            for path in annotation['polygon']['path']:
                x = int(path['x'])
                y = int(path['y'])
                max_y = np.maximum(y, max_y)
                min_y = np.minimum(y, min_y)

                max_x = np.maximum(x, max_x)
                min_x = np.minimum(x, min_x)

                annote_string.append(int(x))
                annote_string.append(int(y))
                annote_s = []
                annote_s.append(annote_string)
            data['annotations'].append({"category_id":obj_id, "image_id":image['id'], "segmentation":annote_s, "id":count, "bbox":[int(min_x),int(min_y),int(max_x-min_x),int(max_y-min_y)], "iscrowd":0})
            count+=1
        else:
            x = int(annotation['keypoint']['x'])
            y = int(annotation['keypoint']['y'])
            annote_string = []
            for i in range(0,3):
                annote_string.append(int(x-(i+1)))
                annote_string.append(int(y+i))
            annote_s = []
            annote_s.append(annote_string)
            data['annotations'].append({"category_id":obj_id, "image_id":image['id'], 'segmentation':annote_s, "id":count, "bbox":[int(x),int(y),2,2], "iscrowd":0})
            count+=1
    



with open(json_location, "w") as jsonFile:
    json.dump(data, jsonFile)

#print(os.listdir(dest))
print(count)


