# WalkWith
시각장애인을 위한 횡단보도 안내 프로젝트 - end2end model을 활용한 횡단보도 검출

## model
   - 참고한 논문 : https://arxiv.org/pdf/1604.07316v1.pdf
   - nvidia에서 차선 사진을 통해 운전 핸들 조정 yaw 값을 추출해내는 end to end 모델을 참고하여 학습하였다.
   - data set이 100정도로 작아서 5000 이상의 epoch을 주면 overfitting이 되어 되려 test에 좋지 않은 결과가 나왔다. 그러므로 5000정도의 epoch으로 학습하였다.
   - train 100번마다 parameter가 pth 파일로 저장되게 하여 라즈베리파이에서는 모델을 제외하고 parameter만 이식할 수 있도록 하였다.

