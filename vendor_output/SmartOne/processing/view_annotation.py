import os
import sys
import cv2
import numpy as np
import imgaug  
 
# Download and install the Python COCO tools from https://github.com/waleedka/coco
# That's a fork from the original https://github.com/pdollar/coco with a bug
# fix for Python 3.
# If the PR is merged then use the original repo.
# Note: Edit PythonAPI/Makefile and replace "python" with "python3".
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from pycocotools import mask as maskUtils
 
from skimage import io
from matplotlib import pyplot as plt
 
 
# Root directory of the project
ROOT_DIR = os.path.abspath("../../")
 
# Import Mask RCNN
sys.path.append(ROOT_DIR)  # To find local version of the library
dataset_dir = "/home/dataset/coco"
subset = "train"
year = "2017"
 
 
coco = COCO("{}/annotations/instances_{}{}.json".format(dataset_dir, subset, year))
catIds = coco.getCatIds(catNms=['person'])
imgIds = coco.getImgIds(catIds=catIds )
imgIds = coco.getImgIds(imgIds = [300784])
img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
 
I = io.imread(img['coco_url'])
plt.axis('off')
plt.imshow(I)
plt.show()
io.imsave(os.path.join(dataset_dir, img['file_name']), I)
 
bg = np.zeros((img['height'], img['width'], 3))
 
plt.imshow(bg)
plt.axis('off')
annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
anns = coco.loadAnns(annIds)
print(img['id'])
coco.showAnns(anns)
plt.show()
 
'''
masks = []
showonce = True
for ann in anns:
    if type(ann['segmentation']) == list and showonce:
        print(ann['segmentation'])
        showonce = False
    if type(ann['segmentation']) != list:
        print(ann['segmentation'])
    m = coco.annToMask(ann)
    coco.showAnns(ann)
    plt.show()
    masks.append(m)
print(len(masks))
'''