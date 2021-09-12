import cv2
import numpy as np


#파일들 다 가져오는 코드
files = []
idx = 1
for i in range(1,5):
  file_name = './new/test8_resized/' + str(i) + ".jpg"
  files.append(file_name)

for image_name in files:
    image = cv2.imread(image_name, cv2.IMREAD_UNCHANGED)
    clone = image.copy()
    resized = cv2.resize(clone, (160, 90), cv2.INTER_AREA)
    cv2.imwrite('./new/test8_resized//%s.jpg'%(idx), resized)
    idx +=1