# 使用sklearn.preprocessing.scale()函数，将给定数据进行标准化
from sklearn import preprocessing
import numpy as np

X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])
X_scaled = preprocessing.scale(X)

X_scaled  