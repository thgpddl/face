# dlib的关键点检测器
1. 主要使用shape_predictor_68_face_landmarks.dat这个文件，本项目没有需要自己去下：
官网下载地址：http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
或者自己百度下载

![image](https://user-images.githubusercontent.com/48787805/111492608-c6236b00-8777-11eb-95d5-3b4697a96814.png)


2. 表现性能

    | 项目 | 数据 | 备注 |
    |  ----  | ----  | ----  |
    | 耗时(s) | 0.001~0.002 | 不包括人脸检测和画点，仅关键点检测和matrix化 |
3. 注意：dlib库的安装，参考：https://blog.csdn.net/qq_41185868/article/details/79678783

