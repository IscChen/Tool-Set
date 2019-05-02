import random
import glob, os
import os.path
import cv2

#---------------------------------------------------------
imageFolder = "/mnt/work/010_01_img_celeba_rev01_0x0_608x608_p202600_n202600/JPEGImages"
outputFolder = "/mnt/work/010_01_img_celeba_rev01_0x0_608x608_p202600_n202600/JPEGImages_gray"
folderCharacter = "/"  # \\ is for windows
#--------------------------------------------------------

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

for file in os.listdir(imageFolder):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension.lower()
    outputFile.append(outputFolder + file)
	
    if(file_extension == ".jpg" or file_extension==".jpeg" or file_extension==".png" or file_extension==".bmp"):
        fileList.append(imageFolder + folderCharacter + file)

    img = cv2.imread(file)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(outputFile, gray)
	

