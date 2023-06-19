import shutil as sh
import natsort
import os
# sh.move(file ,move_path + '/' + file_name)
"""
#코드포머스 만 한거 파일 경로 정리
for sizetext in ['100','200','300','400','500']:        
    path_dir='/home/undergrad_te/siondijun/CodeformersResult_'+sizetext
    save_dir='/home/undergrad_te/siondijun/CodeformersResult_'+sizetext+'_move'
    os.makedirs(save_dir)
    file_list = os.listdir(path_dir)
    file_list=natsort.natsorted(file_list)
    for dataforder in file_list:
        image_list = os.listdir(path_dir+"/"+dataforder+"/final_results")
        image_list=natsort.natsorted(image_list)
        os.makedirs(save_dir+"/"+dataforder)
        for image in image_list:
            sh.copy(path_dir+"/"+dataforder+"/final_results/"+image  ,save_dir+"/"+dataforder + '/' + image)
            
          
   
    
    #최종결과 파일 경로 정리(일단 300까지)
for sizetext in ['400','500']:        
    path_dir='/home/undergrad_te/siondijun/my_Result_'+sizetext
    save_dir='/home/undergrad_te/siondijun/my_Result_'+sizetext+'_move'
    os.makedirs(save_dir)
    file_list = os.listdir(path_dir)
    file_list=natsort.natsorted(file_list)
    for dataforder in file_list:
        image_list = os.listdir(path_dir+"/"+dataforder+"/final_results")
        image_list=natsort.natsorted(image_list)
        os.makedirs(save_dir+"/"+dataforder)
        for image in image_list:
            sh.copy(path_dir+"/"+dataforder+"/final_results/"+image  ,save_dir+"/"+dataforder + '/' + image)
  
#폴더 하나만
path_dir='/home/undergrad_te/siondijun/code_Result_from512LQ_n000001'
save_dir=path_dir+'_move'
os.makedirs(save_dir)
file_list = os.listdir(path_dir+"/final_results")
file_list=natsort.natsorted(file_list)
for image in file_list:
    sh.copy(path_dir+"/final_results/"+image  ,save_dir + '/' + image)
   
    
for sizetext in ['80']:        
    path_dir='/home/undergrad_te/siondijun/my_Result_from_LQ_'+sizetext
    save_dir='/home/undergrad_te/siondijun/my_Result_from_LQ_'+sizetext+'_move'
    os.makedirs(save_dir)
    file_list = os.listdir(path_dir)
    file_list=natsort.natsorted(file_list)
    for dataforder in file_list:
        image_list = os.listdir(path_dir+"/"+dataforder+"/final_results")
        image_list=natsort.natsorted(image_list)
        os.makedirs(save_dir+"/"+dataforder)
        for image in image_list:
            sh.copy(path_dir+"/"+dataforder+"/final_results/"+image  ,save_dir+"/"+dataforder + '/' + image)
   """
   
#코드포머스 만 한거 파일 경로 정리
for sizetext in ['80']:        
    path_dir='/home/undergrad_te/siondijun/my_Result_from_LQ_'+sizetext
    save_dir='/home/undergrad_te/siondijun/my_Result_from_LQ_'+sizetext+'_move'
    os.makedirs(save_dir)
    file_list = os.listdir(path_dir)
    file_list=natsort.natsorted(file_list)
    for dataforder in file_list:
        image_list = os.listdir(path_dir+"/"+dataforder+"/final_results")
        image_list=natsort.natsorted(image_list)
        os.makedirs(save_dir+"/"+dataforder)
        for image in image_list:
            sh.copy(path_dir+"/"+dataforder+"/final_results/"+image  ,save_dir+"/"+dataforder + '/' + image)