import os
import cv2
import natsort
 
    
size_text='80'
test_image_path = '/home/undergrad_te/siondijun/LQimage_'+size_text
guide_image_path='/home/undergrad_te/siondijun/Alignimgs'
landmark_path='/home/undergrad_te/siondijun/Alignimgs_Landmarks'

file_list = os.listdir(test_image_path)
file_list=natsort.natsorted(file_list)
os.mkdir('/home/undergrad_te/siondijun/Testlists_'+size_text)
for dataforder in file_list:
    os.mkdir('/home/undergrad_te/siondijun/Testlists_'+size_text+"/"+dataforder)
    f = open('/home/undergrad_te/siondijun/Testlists_'+size_text+"/"+dataforder+'/'+"TestLists.txt", 'w')
    file_list2 = os.listdir(test_image_path+'/'+dataforder)
    file_list2=natsort.natsorted(file_list2)
    for imgdata in  file_list2:
        
        f.write(test_image_path+'/'+dataforder+'/'+imgdata+'\t'+guide_image_path+"/"+dataforder+'\t'+landmark_path+"/"+dataforder+'\n')        
    f.close()         
       
        
        
        
