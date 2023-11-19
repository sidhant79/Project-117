import os
import cv2

path="C:/WhiteHat jr/Projects/Project 117/PRO-C105-Project-Images-main/PRO-C105-Project-Images-main/Images"
Images = [ ]

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
    
    
    print(file_name)
    Images.append(file_name)
    print("Total frame count :",len(Images))
    count = len(Images)
    frame = cv2.imread(Images[0])

    height, width, channels = frame.shape
    size = (width,height)
    print("Width and height of the frame : ",size)

    out=cv2.VideoWriter('Sun.mp4',cv2.VideoWriter_fourcc(*'DIVX'),5,size)
for i in range(count-1,0,-1):
    frame=cv2.imread(Images[i])
    out.write(frame)

out.release()
print("Done")