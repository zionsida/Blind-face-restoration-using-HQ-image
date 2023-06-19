import numpy
import math
import cv2
import natsort
import os

def psnr(img1, img2):
    mse = numpy.mean( (img1 - img2) ** 2 ) #MSE 구하는 코드
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse)) #PSNR구하는 코드
psnr_list=[];
path_dir = '/home/undergrad_te/siondijun/ASFFNet512/TestExamples/TestResultRestored'
file_list = os.listdir(path_dir)
file_list=natsort.natsorted(file_list)
for dataforder in file_list:
    file_list2 = os.listdir(path_dir+'/'+dataforder)
    file_list2=natsort.natsorted(file_list2)
    for imgdata in  file_list2:
        original = cv2.imread("/home/undergrad_te/siondijun/ASFFNet512/TestExamples/Alignimgs/"+dataforder+"/"+imgdata)
        contrast = cv2.imread("/home/undergrad_te/siondijun/ASFFNet512/TestExamples/TestResultRestored/"+dataforder+"/"+imgdata)
        psnr_list.append(psnr(original,contrast))
print(psnr_list)
mean = sum(psnr_list) / len(psnr_list)
print("평균 PSNR:")
print(mean)
#32.29485638019551   원본-복원

 
