import cv2
import numpy as np
import dlib

face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor('shape_predictor_81_face_landmarks.dat')

img=cv2.imread("face.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_detector(gray)

for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 1)  # 获取人脸框并矩选

    # 关键点检测
    landmarks = landmark_predictor(gray, face)
    landmark = np.matrix([[p.x, p.y] for p in landmarks.parts()])


    for i in range(landmark.__len__()):
        cv2.putText(img,str(i),(landmark[i,0], landmark[i,1]),cv2.FONT_HERSHEY_SIMPLEX,0.3,(0,0,255),1)
        cv2.circle(img, (landmark[i,0], landmark[i,1]), 2, (255,0,0), 1)  # 画点

cv2.imshow("img", img)
cv2.waitKey(0)
