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

import time

from os import listdir
from os import walk
from os.path import isfile, join

from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

mypath=r'C:/Users/ianre/Desktop/coda/aws-labeling/cogito-job/Knot_Tying/'
target=r'C:/Users/ianre/Desktop/coda/aws-labeling/cogito-job/Knot_Tying_mp4/'

def convert_avi_to_mp4(avi_file_path, output_name):
    with suppress_stdout():
        os.popen("C:\\FFmpeg\\bin\\ffmpeg.exe -i " + avi_file_path + " " + output_name + " -loglevel error  -y")
    print("::convert::")
    return True

def convert(avi_file_path, out_file_path):
    ff = ffmpy.FFmpeg(inputs={avi_file_path: None},outputs={out_file_path: None})
    ff.run();



targets = []
dirs = []
f = []
dirpath = mypath
for (dirpath, dirnames, filenames) in walk(mypath):    
    
    f.extend(filenames)  
    dirs.extend(dirnames)
    targets.extend(dirnames)
    #for (dirpath_, dirnames_, filenames_) in walk(dirnames):
    #print(dirpath,'\n', dirnames,'\n', filenames)      
    break

sig_targets = targets.copy()


for i in range(len(dirs)):
    #os.mkdir( os.path.join(target,dirs[i] ) )
    dirs[i] = os.path.join(mypath,dirs[i] ) 
    targets[i] = os.path.join(target,targets[i])
    print("targets,",targets[i])
    

for i in range(len(dirs)):
    #break
    d = dirs[i]
    print("d:",d)

    for(dirpath, dirnames, filenames) in walk(d):
        print(filenames)
        for fn in filenames:
            aviFN = os.path.join(d,fn)
            fn_2 = fn
            #print(fn_2.index("_"), fn_2[fn_2.index("_")])
            #print(fn_2[:fn_2.index("_")] + "_" + sig_targets[i] + fn_2[fn_2.index("_"):] )
            fn_2 = fn_2[:fn_2.index("_")] + "_" + sig_targets[i] + fn_2[fn_2.index("_"):]

            fn = fn_2
            mp4FN = os.path.join(target,fn)

            mp4FN = mp4FN[0:-3] + "mp4"
            convert_avi_to_mp4(aviFN,mp4FN  )
            time.sleep(0.8)
            print('aviFN:',aviFN,"\tmp4FN:",mp4FN)
        break
    
print(dirpath)

for fileName in f:
    break
    print("file found:",fileName)
    aviFile = os.path.join(mypath,fileName)
   
    mp4File = mypath+"mp4/"+str(fileName)
    #mp4File =  os.path.join(mypath,"mp4",fileName)
    mp4File = mp4File[0:-3] + "mp4"
    #f = open(mp4File, "x")
    print("Creating new mp4: ",mp4File)
    #print(aviFile,mp4File)
    
    convert_avi_to_mp4(aviFile,mp4File)

    #convert(aviFile,mp4File)
    #print("converting:  " + mypath+str(fileName))
    #print(fileName)