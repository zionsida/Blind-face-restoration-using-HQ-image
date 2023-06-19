
import numpy
from PIL import Image, ImageDraw
import numpy as np;
import os
import natsort
from tqdm import tqdm
for size_text in ["80"]:

    #/home/undergrad_te/siondijun/ASFFNet512/TestExamples/Alignimgs_Landmarks/n000001/0004_01.jpg.png.txt
    land_dir = '/home/undergrad_te/siondijun/ASFFNetResult_'+size_text+'_Landmarks/'#랜드마크 폴더/
    save_path='/home/undergrad_te/siondijun/ASFFNet_facecccv_to_low'
    asff_path='/home/undergrad_te/siondijun/ASFFNetResult_'+size_text
    low_path='/home/undergrad_te/siondijun/LQ512_from_'+size_text
    #low_path='/home/undergrad_te/siondijun/LQimages/LQ512_from_'+size_text
    file_list = os.listdir(land_dir)
    file_list=natsort.natsorted(file_list)
    os.mkdir(save_path+size_text)
    for dataforder in tqdm(file_list):
        print(dataforder)
        os.mkdir(save_path+size_text+'/'+dataforder)#저장경로
        file_list2 = os.listdir(land_dir+'/'+dataforder)
        for imgdata in  file_list2:
            if os.path.isfile(asff_path+"/"+dataforder+"/"+imgdata.strip(".txt")):#자를 이미지 파일경로
                txtland_dir =land_dir+dataforder+"/"+imgdata                 #텍스트 파일 경로
                
                im = Image.open(asff_path+"/"+dataforder+"/"+imgdata.strip(".txt")).convert("RGBA")#자를 이미지 파일경로
                im2=Image.open(low_path+"/"+dataforder+"/"+imgdata.strip(".txt")).convert("RGBA")          #low이미지 경로 건들 ㄴㄴ
            
                with open(txtland_dir) as f:
                    lines = f.read().splitlines()
                #print(lines)
                randmarklist1 = [0 for i in range(28)]
                randmarklist2 = [0 for i in range(28)]
                for i in range(28):
                    linesplit=lines[i].split()
                    randmarklist1[i]=linesplit[0]
                    randmarklist2[i]=linesplit[1]
                randmarklist = [0 for i in range(27)]
                for i in range(18):
                    randmarklist[i]=((float(randmarklist1[i]),float(randmarklist2[i])))
                for i in range(10):
                    randmarklist[i+17]=((float(randmarklist1[26-i]),float(randmarklist2[26-i])))
                #print(randmarklist)


                # convert to numpy (for convenience)
                imArray = numpy.asarray(im)
                # create mask
                polygon = randmarklist
                maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
                ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
                mask = numpy.array(maskIm)
                # assemble new image (uint8: 0-255)
                newImArray = numpy.empty(imArray.shape,dtype='uint8')
                # colors (three first columns, RGB)
                newImArray[:,:,:3] = imArray[:,:,:3]
                # transparency (4th column)
                newImArray[:,:,3] = mask*255
                # back to Image from numpy
                newIm = Image.fromarray(newImArray, "RGBA")
                im2.paste(newIm, (0, 0), newIm)
                im2.save(save_path+size_text+'/'+dataforder+"/"+imgdata.strip(".txt"))
                #newIm.save("/home/undergrad_te/siondijun/out.png")
            