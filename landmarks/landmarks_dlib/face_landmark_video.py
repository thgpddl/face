import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)

face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

while True:
    _, frame = cap.read()

    # 人脸检测
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)  # 获取人脸框并矩选

        # 关键点检测
        landmarks = landmark_predictor(gray, face)
        landmark = np.matrix([[p.x, p.y] for p in landmarks.parts()])
        for i in range(landmark.__len__()):
            cv2.putText(frame,str(i),(landmark[i,0], landmark[i,1]),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,255),1)
            cv2.circle(frame, (landmark[i,0], landmark[i,1]), 2, (255,0,0), 1)  # 画点
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()