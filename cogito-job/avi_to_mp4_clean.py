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

#import ffmpy


#C:\Users\ianre\Desktop\Academica\Research\s_aw_demo\G9_sub
vid_place='C:/Users/ianre/Desktop/Academica/Research/s_aw_demo/G9_sub/*'
mypath=r'C:/Users/ianre/Desktop/Academica/Research/s_aw_demo/G9_sub/'
print(vid_place)

#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


def convert_avi_to_mp4(avi_file_path, output_name):
    #os.popen("C:\\FFmpeg\\bin\\ffmpeg.exe -i '{input}' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(input = avi_file_path, output = output_name))
    #os.popen("C:\\FFmpeg\\bin\\ffmpeg.exe -i " + avi_file_path + " -c:v copy -c:a copy -y " + output_name)
    os.popen("C:\\FFmpeg\\bin\\ffmpeg.exe -i " + avi_file_path + " " + output_name)
    print("::convert::")
    return True

def convert(avi_file_path, out_file_path):
    ff = ffmpy.FFmpeg(inputs={avi_file_path: None},outputs={out_file_path: None})
    ff.run();

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