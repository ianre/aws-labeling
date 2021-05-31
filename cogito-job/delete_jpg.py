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


root=r'C:/Users/ianre/Desktop/coda/aws-labeling/cogito-job/slicing_tests/29s'


def deleteJPEG(dir):
    
    for(dirpath, dirnames, filenames) in walk(dir):
        #print("filename:",filenames)
        for f in filenames:
            term = f[-4:]
            if(term == ".jpg"):
                print("term:",term)
                os.remove(os.path.join(root,f))
            #print(term)

        return
    return
    command = "C:\\FFmpeg\\bin\\ffprobe.exe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 " + dirname

deleteJPEG(root)