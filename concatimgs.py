import cv2
import os.path as osp
import os
import natsort




#['80','100','200','300','400','500']


file_resolutions = ['80']
for sizetext in file_resolutions: 
    filelistpath='/home/undergrad_te/siondijun/my_Result_from_LQ_'+sizetext
    file_list = os.listdir(filelistpath)
    file_list=natsort.natsorted(file_list)
    for file in file_list:
        imglist = os.listdir(filelistpath+"/"+file)
        imglist=natsort.natsorted(imglist)
        os.makedirs('/home/undergrad_te/siondijun/all_result_80/'+file)
        for image in imglist:
            img1=cv2.imread('/home/undergrad_te/siondijun/Alignimgs/'+file+'/'+image)
            img2=cv2.imread('/home/undergrad_te/siondijun/ASFFNetResult_'+sizetext+'+guid_move'+'/'+file+'/'+image)
            img3=cv2.imread('/home/undergrad_te/siondijun/CodeformersResult_'+sizetext+'/'+file+'/'+image)
            img4=cv2.imread('/home/undergrad_te/siondijun/ASFFNet_facecccv_to_coderesult_'+sizetext+'/'+file+'/'+image)
            new=cv2.hconcat([img1,img2,img3,img4])
            cv2.imwrite('/home/undergrad_te/siondijun/all_result_80/'+file+'/'+image,new)