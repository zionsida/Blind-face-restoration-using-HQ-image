import os
import cv2
"""
        
        
path_dir = '/home/undergrad_te/siondijun/Alignimgs'
file_list = os.listdir(path_dir)
size_int=100
size_text='100'
os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text)
for dataforder in file_list:
    os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder)
    file_list2 = os.listdir(path_dir+'/'+dataforder)
    for imgdata in  file_list2:
        img_name = path_dir + '/' +dataforder+'/'+ imgdata
        img = cv2.imread(img_name, cv2.IMREAD_COLOR)
        h,w,c = img.shape
        #이미지 해상도 줄이기 
        resizeimg = cv2.resize(img, dsize=(size_int, size_int), interpolation=cv2.INTER_AREA)
        #저장
        cv2.imwrite("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder+"/"+imgdata,resizeimg)


file_list = os.listdir(path_dir)
size_int=200
size_text='200'
os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text)
for dataforder in file_list:
    os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder)
    file_list2 = os.listdir(path_dir+'/'+dataforder)
    for imgdata in  file_list2:
        img_name = path_dir + '/' +dataforder+'/'+ imgdata
        img = cv2.imread(img_name, cv2.IMREAD_COLOR)
        h,w,c = img.shape
        #이미지 해상도 줄이기 
        resizeimg = cv2.resize(img, dsize=(size_int, size_int), interpolation=cv2.INTER_AREA)
        #저장
        cv2.imwrite("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder+"/"+imgdata,resizeimg)

file_list = os.listdir(path_dir)
size_int=300
size_text='300'
os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text)
for dataforder in file_list:
    os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder)
    file_list2 = os.listdir(path_dir+'/'+dataforder)
    for imgdata in  file_list2:
        img_name = path_dir + '/' +dataforder+'/'+ imgdata
        img = cv2.imread(img_name, cv2.IMREAD_COLOR)
        h,w,c = img.shape
        #이미지 해상도 줄이기 
        resizeimg = cv2.resize(img, dsize=(size_int, size_int), interpolation=cv2.INTER_AREA)
        #저장
        cv2.imwrite("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder+"/"+imgdata,resizeimg)

file_list = os.listdir(path_dir)
size_int=400
size_text='400'
os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text)
for dataforder in file_list:
    os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder)
    file_list2 = os.listdir(path_dir+'/'+dataforder)
    for imgdata in  file_list2:
        img_name = path_dir + '/' +dataforder+'/'+ imgdata
        img = cv2.imread(img_name, cv2.IMREAD_COLOR)
        h,w,c = img.shape
        #이미지 해상도 줄이기 
        resizeimg = cv2.resize(img, dsize=(size_int, size_int), interpolation=cv2.INTER_AREA)
        #저장
        cv2.imwrite("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder+"/"+imgdata,resizeimg)

file_list = os.listdir(path_dir)
size_int=500
size_text='500'
os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text)
for dataforder in file_list:
    os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder)
    file_list2 = os.listdir(path_dir+'/'+dataforder)
    for imgdata in  file_list2:
        img_name = path_dir + '/' +dataforder+'/'+ imgdata
        img = cv2.imread(img_name, cv2.IMREAD_COLOR)
        h,w,c = img.shape
        #이미지 해상도 줄이기 
        resizeimg = cv2.resize(img, dsize=(size_int, size_int), interpolation=cv2.INTER_AREA)
        #저장
        cv2.imwrite("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder+"/"+imgdata,resizeimg)
  """
  
path_dir = '/home/undergrad_te/siondijun/Alignimgs'
file_list = os.listdir(path_dir)
size_int=50
size_text='50'
os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text)
for dataforder in file_list:
    os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder)
    file_list2 = os.listdir(path_dir+'/'+dataforder)
    for imgdata in  file_list2:
        img_name = path_dir + '/' +dataforder+'/'+ imgdata
        img = cv2.imread(img_name, cv2.IMREAD_COLOR)
        h,w,c = img.shape
        #이미지 해상도 줄이기 
        resizeimg = cv2.resize(img, dsize=(size_int, size_int), interpolation=cv2.INTER_AREA)
        #저장
        cv2.imwrite("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder+"/"+imgdata,resizeimg)
path_dir = '/home/undergrad_te/siondijun/Alignimgs'
file_list = os.listdir(path_dir)
size_int=80
size_text='80'
os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text)
for dataforder in file_list:
    os.mkdir("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder)
    file_list2 = os.listdir(path_dir+'/'+dataforder)
    for imgdata in  file_list2:
        img_name = path_dir + '/' +dataforder+'/'+ imgdata
        img = cv2.imread(img_name, cv2.IMREAD_COLOR)
        h,w,c = img.shape
        #이미지 해상도 줄이기 
        resizeimg = cv2.resize(img, dsize=(size_int, size_int), interpolation=cv2.INTER_AREA)
        #저장
        cv2.imwrite("/home/undergrad_te/siondijun/LQimage_"+size_text+"/"+dataforder+"/"+imgdata,resizeimg)
