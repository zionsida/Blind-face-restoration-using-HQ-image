import os
import natsort
import cv2
#,
for size_text in ["80"]:
    lowpath = '/home/undergrad_te/siondijun/LQimage_'+size_text
    print(lowpath)
    file_list = os.listdir(lowpath)
    file_list=natsort.natsorted(file_list)
    savelowpath="/home/undergrad_te/siondijun/LQ512_from_"+size_text
    print(savelowpath)
    os.mkdir(savelowpath)
    for dataforder in file_list:
        os.mkdir(savelowpath+"/"+dataforder)
        file_list2 = os.listdir(lowpath+'/'+dataforder)
        file_list2=natsort.natsorted(file_list2)
        for imgdata in  file_list2:
            imgpath=lowpath+"/"+dataforder+"/"+imgdata
            img = cv2.imread(imgpath)
            img=cv2.resize(img,(512,512))
            cv2.imwrite(savelowpath+"/"+dataforder+"/"+imgdata,img)
            #img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
            #img512=img.resize((512,512))
            #cv2.imwrite("/home/undergrad_te/siondijun/low_512/"+dataforder+"/"+imgdata,img512)