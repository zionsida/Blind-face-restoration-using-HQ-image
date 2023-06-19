import os
import natsort
import cv2
path_dir = '/home/undergrad_te/siondijun/ASFFNet512/TestExamples/LQCrob'
file_list = os.listdir(path_dir)
file_list=natsort.natsorted(file_list)
for dataforder in file_list:
    os.mkdir("/home/undergrad_te/siondijun/low_512/"+dataforder)
    file_list2 = os.listdir(path_dir+'/'+dataforder)
    file_list2=natsort.natsorted(file_list2)
    for imgdata in  file_list2:
        imgpath=path_dir+"/"+dataforder+"/"+imgdata
        img = cv2.imread(imgpath)
        img=cv2.resize(img,(512,512))
        cv2.imwrite("/home/undergrad_te/siondijun/low_512/"+dataforder+"/"+imgdata,img)
        #img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
        #img512=img.resize((512,512))
        #cv2.imwrite("/home/undergrad_te/siondijun/low_512/"+dataforder+"/"+imgdata,img512)