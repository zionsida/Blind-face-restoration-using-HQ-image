import os
import cv2
path_dir = '/home/undergrad_te/siondijun/data/archive (3)'
file_list = os.listdir(path_dir)

os.mkdir('/home/undergrad_te/siondijun/originimg')
for dataforder in file_list:
    os.mkdir('/home/undergrad_te/siondijun/originimg/'+dataforder)
    file_list2 = os.listdir(path_dir+'/'+dataforder)
    for imgdata in  file_list2:
        img_name = path_dir + '/' +dataforder+'/'+ imgdata
        img = cv2.imread(img_name, cv2.IMREAD_COLOR)
        h,w,c = img.shape
        if 1024>h>512:
            if 1024>w>512:
                cv2.imwrite("/home/undergrad_te/siondijun/originimg/"+dataforder+"/"+imgdata+".jpg",img)

