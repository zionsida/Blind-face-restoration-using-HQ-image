
import numpy
from PIL import Image, ImageDraw
import numpy as np;
import os
import natsort
from tqdm import tqdm

im = Image.open('/home/undergrad_te/siondijun/ASFFNetResult_80/n000148/0026_01.jpg.png').convert("RGBA") #자를 이미지 파일경로
im2=Image.open('/home/undergrad_te/siondijun/white.png').convert("RGBA")          #low이미지 경로 건들 ㄴㄴ

with open('/home/undergrad_te/siondijun/ASFFNetResult_80_Landmarks/n000148/0026_01.jpg.png.txt') as f:
    lines = f.read().splitlines()
#print(lines)
randmarklist1 = [0 for i in range(28)]
randmarklist2 = [0 for i in range(28)]
for i in range(28):
    linesplit=lines[i].split()
    randmarklist1[i]=linesplit[0]
    randmarklist2[i]=linesplit[1]
randmarklist = [0 for i in range(27)]
for i in range(18):
    randmarklist[i]=((float(randmarklist1[i]),float(randmarklist2[i])))
for i in range(10):
    randmarklist[i+17]=((float(randmarklist1[26-i]),float(randmarklist2[26-i])))
#print(randmarklist)


# convert to numpy (for convenience)
imArray = numpy.asarray(im)
# create mask
polygon = randmarklist
maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
mask = numpy.array(maskIm)
# assemble new image (uint8: 0-255)
newImArray = numpy.empty(imArray.shape,dtype='uint8')
# colors (three first columns, RGB)
newImArray[:,:,:3] = imArray[:,:,:3]
# transparency (4th column)
newImArray[:,:,3] = mask*255
# back to Image from numpy
newIm = Image.fromarray(newImArray, "RGBA")
im2.paste(newIm, (0, 0), newIm)
im2.save('/home/undergrad_te/siondijun/z.png')
#newIm.save("/home/undergrad_te/siondijun/out.png")
