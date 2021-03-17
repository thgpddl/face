# 基于Dlib库68个特征点的基础上，增加了13个特征点(共81个) ，把前额也包含在追踪范围里
![image](https://user-images.githubusercontent.com/48787805/111491097-8ad46c80-8776-11eb-97a0-59d6f2f1adb8.png)

可以看出该模型的确包含了前额关键点，但比如嘴部关键点的精度，还是dlib表现更好
1. 新闻介绍：https://baijiahao.baidu.com/s?id=1628339297294302540&wfr=spider&for=pc
2. 源github项目：https://github.com/coronadoapps/Face-Recognition-Python-OpenCV
3. 需要的库：numpy、dlib、opencv-python
4. 表现性能

    | 项目 | 数据 | 备注 |
    |  ----  | ----  | ----  |
    | 耗时(s) | 0.001~0.002 | 不包括人脸检测和画点，仅关键点检测和matrix化 |

5. 注意：dlib库的安装，参考：https://blog.csdn.net/qq_41185868/article/details/79678783

