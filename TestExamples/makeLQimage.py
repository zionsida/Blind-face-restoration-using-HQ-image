import os
import cv2
path_dir = '/home/undergrad_te/siondijun/Alignimgs'
file_list = os.listdir(path_dir)


for dataforder in file_list:
    os.mkdir('/home/undergrad_te/siondijun/LQimage/'+dataforder)
    file_list2 = os.listdir(path_dir+'/'+dataforder)
    for imgdata in  file_list2:
        img_name = path_dir + '/' +dataforder+'/'+ imgdata
        img = cv2.imread(img_name, cv2.IMREAD_COLOR)
        h,w,c = img.shape
        #이미지 해상도 줄이기 
        resizeimg = cv2.resize(img, dsize=(256, 256), interpolation=cv2.INTER_AREA)
        #저장
        cv2.imwrite("/home/undergrad_te/siondijun/LQimage/"+dataforder+"/"+imgdata,resizeimg)