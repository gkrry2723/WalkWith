import cv2
import argparse
import numpy as np
import csv

#파일들 다 가져오는 코드
files = []
idx = 1
for i in range(1,5):
  file_name = './new/test8_resized/' + str(i) + ".jpg"
  files.append(file_name)

clicked_points = []
all_points = []
clone = None

def MouseLeftClick(event, x, y, flags, param):
	# 왼쪽 마우스가 클릭되면 (x, y) 좌표를 저장한다.
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((y, x))
        print(clicked_points)

		# 원본 파일을 가져 와서 clicked_points에 있는 점들을 그린다.
        image = clone.copy()
        for point in clicked_points:
            cv2.circle(image, (point[1], point[0]), 2, (0, 255, 255), thickness = -1)
        cv2.imshow("image", image)

count = 1
f = open('new/test.csv','w')
wr = csv.writer(f)

# 새 윈도우 창을 만들고 그 윈도우 창에 click_and_crop 함수를 세팅해 줍니다.
cv2.namedWindow("image")
cv2.setMouseCallback("image", MouseLeftClick)

for idx, image_name in enumerate(files):
  #for i in range(4):
    image = cv2.imread(image_name)  # 이미지 불러오기
    clone = image.copy()

    flag = False

    while True:
        cv2.imshow("image", image)
        key = cv2.waitKey(0)

        # n 하면 다음 사진으로 넘어가기
        if key == ord('n'):
            all_points.append(clicked_points)

            wr.writerow([count,list(clicked_points[0]),list(clicked_points[1]),list(clicked_points[2]),list(clicked_points[3])])
            count += 1
            print("----", clicked_points)
            # 클릭한 점 초기화
            
            if count == 25:
                  flag = True
                  wr.writerow([count,list(clicked_points[0]),list(clicked_points[1]),list(clicked_points[2]),list(clicked_points[3])])
                  f.close()
                  break
            clicked_points = []

            break

        # q 누르면 프로그램 종료됨
        if key == ord('q'):
            # 프로그램 종료
            flag = True
            wr.writerow([count,list(clicked_points[0]),list(clicked_points[1]),list(clicked_points[2]),list(clicked_points[3])])
            f.close()
            break
        
        # z 누르면 이전으로 되돌아가기 가능
        if key == ord('z'):
            clicked_points.pop(-1)

    if flag:
        break

# 모든 window를 종료합니다.
cv2.destroyAllWindows()

print(all_points)