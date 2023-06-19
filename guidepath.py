
import os
import natsort
import shutil as sh

file_resolutions = ['100','200','300','400','500']
for sizetext in file_resolutions: 
    filelistpath='/home/undergrad_te/siondijun/ASFFNetResult_'+sizetext+'+guid'
    file_list = os.listdir(filelistpath)
    file_list=natsort.natsorted(file_list)
    for file in file_list:
        image_list = os.listdir(filelistpath+"/"+file)
        image_list=natsort.natsorted(image_list)
        savepath=filelistpath+"_move"+"/"+file[0:7]
        print(savepath)
        os.makedirs(savepath)
        for image in image_list:
            print(filelistpath+'/'+file + "/" + image )
            print(savepath + "/" + image)
            sh.copy(filelistpath+'/'+file + "/" + image ,savepath + "/" + image)
