import numpy
from PIL import Image, ImageDraw

import numpy as np;
path_dir ="/home/undergrad_te/siondijun/ASFFNet512/TestExamples/Alignimgs_Landmarks/n000001/0007_01.jpg.png.txt"
with open(path_dir) as f:
    lines = f.read().splitlines()
print(lines)
randmarklist1 = [0 for i in range(28)]
randmarklist2 = [0 for i in range(28)]
for i in range(28):
    linesplit=lines[i].split()
    randmarklist1[i]=linesplit[0]
    randmarklist2[i]=linesplit[1]
randmarklist = [0 for i in range(28)]
for i in range(18):
    randmarklist[i]=((float(randmarklist1[i]),float(randmarklist2[i])))
for i in range(10):
    randmarklist[i+18]=((float(randmarklist1[27-i]),float(randmarklist2[27-i])))
print(randmarklist)