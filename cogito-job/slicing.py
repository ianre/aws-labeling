import cv2
import os

import glob
import os
import json
import pandas as pd
from tkinter import *
global index
global current_file
global error
from datetime import datetime

DEBUG = False

from os import listdir
from os import walk
from os.path import isfile, join

from subprocess import check_output
from subprocess import Popen, PIPE


root=r'C:/Users/ianre/Desktop/coda/aws-labeling2/cogito-job/slicing_tests/'

s0=os.path.join(root,"0s")
s1=os.path.join(root,"1s")
s11=os.path.join(root,"11s")
s22=os.path.join(root,"22s")
s29=os.path.join(root,"29s")
target=os.path.join(s29,"KnotTying_G15_sub_G002_1220_2103.mp4")
json_location = os.path.join(root, "slice_record.json")

data = {}
if not os.path.exists(json_location):
    #os.mknod(json_location)
    open(json_location,'x')

with open(json_location, "w") as outfile:
    json.dump(data, outfile)

with open(json_location) as f:
    data = json.load(f)

vidcap = cv2.VideoCapture(target)
success,image = vidcap.read()
count = 0

while success:
    break
    cv2.imwrite("C:/Users/ianre/Desktop/coda/aws-labeling/cogito-job/slicing_tests/29s/frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    if success:
        os.remove("C:/Users/ianre/Desktop/coda/aws-labeling/cogito-job/slicing_tests/29s/frame%d.jpg" % count)
    print('Read a new frame: ', success," frame%d.jpg" % count)
    count += 1

def get_frames():
    print("get_frames for target:",target)
    cap = cv2.VideoCapture(target)
    i = 0
    # a variable to set how many frames you want to skip
    frame_skip = 1
    while cap.isOpened():

        ret, frame = cap.read()
        print("i:",i,"\tret:",ret,"\tframe:","-","\tcap:",cap)
        if not ret:
            print("\t\t\t\tbreak:")
            break
        
        if i > frame_skip - 1:
            cv2.imwrite('C:/Users/ianre/Desktop/coda/aws-labeling2/cogito-job/slicing_tests/29s/test_'+str(i)+'.jpg', frame)
            i = 0
            print('C:/Users/ianre/Desktop/coda/aws-labeling2/cogito-job/slicing_tests/29s/test_'+str(i)+'.jpg')
            continue
        i += 1

    cap.release()
    cv2.destroyAllWindows()



def slice_gestures(gestures_path):
    '''
    Wrapper for get_all_frames() which looks at all of the gestures inside the folder gestures_path
    '''
    for(dirpath, dirnames, filenames) in walk(gestures_path):
        # dirnames contains all directories in gestures_path
                
        for d in dirnames:
            dir = os.path.join(gestures_path,d)            
            #data.append(sliceAndRecord(dir))
            data[d] = sliceAndRecord(dir)
        break

def sliceAndRecord(dir):
    '''
    This method extracts the frames one of the files in the directory dir and creates a folder to save all the frames
    '''    
    for(dirpath, dirnames, filenames) in walk(dir):
        video_data = list()
        for f in filenames:
            # make the directories    
            video_fold = os.path.join(dir,f.split(".")[0])            
            video = os.path.join(dir,f)
            video_info = {}
            video_info["name"] = f.split(".")[0]
            if not os.path.exists(video_fold):
                os.makedirs(video_fold)
            print("reading file:",video)
            cap = cv2.VideoCapture(video)
            i = 0
            saved_i = 0
            tf = totalFrames(video)
            video_info["total_frames"] = tf
            # a variable to set how many frames you want to skip
            frame_skip = 1
            frame_data = []

            while cap.isOpened():
                
                ret, frame = cap.read()
                print("i:",i,"\tret:",ret,"\tframe:","-","\tcap:",cap)
                if not ret:
                    print("\t\t\t\tbreak:")
                    break
                #check if directory exists:    
                
                if(i==0 or i==tf-1 or keepFrame(i,tf)):
                    save_frame = os.path.join(video_fold,"frame_"+getIndexString(str(saved_i))+".png" )
                    #frame_data.append([i , "frame_"+getIndexString(str(i)), True])
                    frame_data.append([i ,saved_i])
                    if not DEBUG:
                        cv2.imwrite(save_frame, frame) 
                        print("saved frame:",save_frame)
                    saved_i += 1        
                else: 
                    #frame_data.append([i , "frame_"+getIndexString(str(i)), ""])
                    frame_data.append([i , ""])
                #print("save_frame:",save_frame)

                i += 1
                
                #cv2.imwrite('C:/Users/ianre/Desktop/coda/aws-labeling/cogito-job/slicing_tests/29s/test_'+str(i)+'.jpg', frame)
                
            video_info["frames"] = frame_data
            video_data.append(video_info)
            cap.release()
            cv2.destroyAllWindows()        
        return video_data

        
def keepFrame(index, total):

    if(abs(index-total)<6): return False

    mod15 = index%15==0
    if(total>35):
        return mod15
    elif(total>15):
        return index%12==0
    elif(total>8):
        return index%6==0

    return False


def get_all_frames(dir):
    '''
    This method extracts the frames one of the files in the directory dir and creates a folder to save all the frames
    '''
    
    for(dirpath, dirnames, filenames) in walk(dir):

        for f in filenames:

            # make the directories
            #os.makedirs("")
            
            video_fold = os.path.join(dir,f.split(".")[0])
            video = os.path.join(dir,f)
            if not os.path.exists(video_fold):
                os.makedirs(video_fold)
            print("reading file:",video)
            cap = cv2.VideoCapture(video)
            i = 0
            # a variable to set how many frames you want to skip
            frame_skip = 1
            while cap.isOpened():
                ret, frame = cap.read()
                print("i:",i,"\tret:",ret,"\tframe:","-","\tcap:",cap)
                if not ret:
                    print("\t\t\t\tbreak:")
                    break
                i += 1
                #check if directory exists:    
                save_frame = os.path.join(video_fold,f.split(".")[0]+"_frame_"+getIndexString(str(i))+".png" )
                print("save_frame:",save_frame)
                #cv2.imwrite('C:/Users/ianre/Desktop/coda/aws-labeling/cogito-job/slicing_tests/29s/test_'+str(i)+'.jpg', frame)
                cv2.imwrite(save_frame, frame)
            cap.release()
            cv2.destroyAllWindows()
        break

def getIndexString(i):
    if len(str(i)) >= 4:
        return i
    else:
        return getIndexString("0"+i)

def getFrameCountDir(dirname):
    
    for(dirpath, dirnames, filenames) in walk(dirname):
        #print("filename:",filenames)
        for f in filenames:
            filename = os.path.join(dirname, f)

            command = "C:\\FFmpeg\\bin\\ffprobe.exe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 " + filename
            
            #print(out)
            total_fames = 0
            video_count = 0 

            p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, err = p.communicate(b"input data that is passed to subprocess' stdin")
            rc = p.returncode
            
            print("Video #", video_count, " : ", int(output))
            total_fames +=  int(output)
            video_count += 1

    return total_fames, video_count 

def getFrameCount(filename):

    command = "C:\\FFmpeg\\bin\\ffprobe.exe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 " + filename
    #print(command)

    #out = check_output([command])
    #text = pipe.communicate()[0]
    #print(out)
    total_fames = 0
    video_count = 0 

    p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    rc = p.returncode
    
    #print("Video #", video_count, " : ", int(output))
    total_fames +=  int(output)
    video_count += 1
    return total_fames, video_count 

def totalFrames(filename):
    command = "C:\\FFmpeg\\bin\\ffprobe.exe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 " + filename
    total_fames = 0
    p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    rc = p.returncode        
    total_fames +=  int(output)
    return total_fames

#get_all_frames()

print("counting Frames of target:",target)
#getFrameCount(target)


print("counting frames of directory:",s0)
#getFrameCountDir(s0)

print("get_frames for dir:",s0)
#get_all_frames(s0)
slice_gestures(root)


#print("data:",data)
print("json_location:",json_location)
with open(json_location, "w") as jsonFile:
    json.dump(data, jsonFile)