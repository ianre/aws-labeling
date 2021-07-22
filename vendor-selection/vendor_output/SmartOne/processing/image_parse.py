import os
import shutil
import json
import numpy as np


src = os.path.dirname(os.path.realpath(__file__))
dest = os.path.dirname(os.path.realpath(__file__))
count = 1
scale_x = 6.45
scale_y = 4.85
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
    with open('annotations.json') as file:
        annotations = json.load(file)
    for annotation in annotations:
        file_upload = annotation['file_upload']
        p = file_upload[:-13]

        #print(p,":",image['file_name'][:-5])
        if(p==image['file_name'][:-5]):
            print("found",len(annotation['annotations'][0]['result']))
            #annotation has 12 objects = 12 annotes
            for result in annotation['annotations'][0]['result']:
                #print(annote)
                #print(result['type'])
                
                c_id =  result['type']
                #print(c_id )
                obj_id = 0
                

                if c_id=='polygonlabels':
                    annote_string = []
                    max_y = 0 
                    max_x = 0
                    min_x = 1000
                    min_y = 1000 

                    #print(result['value']['polygonlabels'][0])
                    if result['value']['polygonlabels'][0]=="Left grasper":
                        obj_id = 302802
                    elif result['value']['polygonlabels'][0] =="Right grasper":
                        obj_id = 302803

                    for points in result['value']['points']:
                        x = int(points[0]) * scale_x
                        y = int(points[1]) * scale_y
                        #print(x,y)
                        max_y = np.maximum(y, max_y)
                        min_y = np.minimum(y, min_y)

                        max_x = np.maximum(x, max_x)
                        min_x = np.minimum(x, min_x)
                        
                        annote_string.append(int(x))
                        annote_string.append(int(y))
                        annote_s = []
                        annote_s.append(annote_string)
                        print(annote_s)
                        # points is an array of [x,y]
                    data['annotations'].append({"category_id":obj_id, "image_id":image['id'], "segmentation":annote_s, "id":count, "bbox":[int(min_x),int(min_y),int(max_x-min_x),int(max_y-min_y)], "iscrowd":0})
                    count+=1
                else:                  
                    #print(result['value']['keypointlabels'][0])     
                    x = int(result['value']['x']) * scale_x
                    y = int(result['value']['y']) * scale_y
                    annote_string = []
                    for i in range(0,3):
                        annote_string.append(int(x+(i+1)))
                        annote_string.append(int(y+i))
                    annote_s = []
                    annote_s.append(annote_string)

                    if result['value']['keypointlabels'][0]=="Needle end":
                        obj_id = 302804
                    elif result['value']['keypointlabels'][0]=="Needle Tip":
                        obj_id= 302805
                    data['annotations'].append({"category_id":obj_id, "image_id":image['id'], 'segmentation':annote_s, "id":count, "bbox":[int(x),int(y),2,2], "iscrowd":0})
                    count+=1
                
                #print(obj_id)

            

with open(json_location, "w") as jsonFile:
    json.dump(data, jsonFile)

#print(os.listdir(dest))
print(count)


