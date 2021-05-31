# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:08:55 2021

@author: ianre
"""

import glob
import os
import pandas as pd
from tkinter import *
global index
global current_file
global error
from datetime import datetime

from os import listdir
from os import walk
from os.path import isfile, join

from subprocess import check_output
from subprocess import Popen, PIPE



#import ffmpy

#vid_place='C:/Users/ianre/Desktop/Academica/Research/aws raw videos/JIGSAWS_needlepassing/G4_sub/*'
#mypath=r'C:/Users/ianre/Desktop/Academica/Research/aws raw videos/JIGSAWS_needlepassing/G4_sub/'
vid_place='C:/Users/ianre/Desktop/Academica/Research/aws_videos/JIGSAWS_needlepassing/*'
#mypath=r'C:/Users/ianre/Desktop/Academica/Research/aws_videos/JIGSAWS_needlepassing/'
mypath=r'C:\\Users\\ianre\\Desktop\\Academica\\Research\\aws_videos\\JIGSAWS_suturing'
#JIGSAWS_suturing

print(vid_place)

total_fames = 0
video_count = 0
for root, dirs, files in os.walk(mypath):
     for file in files:
        with open(os.path.join(root, file), "r") as auto:
            #print(auto.name)
            #os.popen("C:\\FFmpeg\\bin\\ffmpeg.exe -i " + avi_file_path + " " + output_name)
            # pipe = os.popen("C:\\FFmpeg\\bin\\ffprobe.exe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 " + auto.name, stdout=PIPE)
            #ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 NeedlePassing_B001_1632_1775.mp4
            command = "C:\\FFmpeg\\bin\\ffprobe.exe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 " + auto.name
            #print(command)

            #out = check_output([command])
            #text = pipe.communicate()[0]
            #print(out)

            p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, err = p.communicate(b"input data that is passed to subprocess' stdin")
            rc = p.returncode
            
            print("Video #", video_count, " : ", int(output))
            total_fames +=  int(output)
            video_count += 1


print("Total Video Count: ", video_count)
print("Total Frame Count: ", total_fames)
quit()


def convert_avi_to_mp4(avi_file_path, output_name):
    #os.popen("C:\\FFmpeg\\bin\\ffmpeg.exe -i '{input}' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(input = avi_file_path, output = output_name))
    os.popen("C:\\FFmpeg\\bin\\ffmpeg.exe -i " + avi_file_path + " " + output_name)
    print("::convert::")
    return True

def convert(avi_file_path, out_file_path):
    #ff = ffmpy.FFmpeg(inputs={avi_file_path: None},outputs={out_file_path: None})
    #ff.run();
    print("bruh")

f = []
for (dirpath, dirnames, filenames) in walk(mypath):    
    f.extend(filenames)        
    break



for fileName in f:
    
    aviFile = os.path.join(mypath,fileName)
   
    mp4File = mypath+"mp4/"+str(fileName)
    #mp4File =  os.path.join(mypath,"mp4",fileName)
    mp4File = mp4File[0:-3] + "mp4"
    print(aviFile,mp4File)
    
    convert_avi_to_mp4(aviFile,mp4File)
    #convert(aviFile,mp4File)
    #print("converting:  " + mypath+str(fileName))
    #print(fileName)
