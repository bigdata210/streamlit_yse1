# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import joblib  # 모델 저장 도는 불러올 때

data = pd.read_csv("data/iris.csv")
le = LabelEncoder()
print(le.fit(data['species']))
data['species'] = le.fit_transform(data['species'])
print(le.classes_) # ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']

# train set, test set 분리
X = data.drop(columns = ['species'])
y = data['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
print(X_train.shape, X_train.ndim)

# 모델 생성
model = LogisticRegression()
model.fit(X_train, y_train)

# 모델 만들고 배포 (Export)
model_file = open("models/logistic_regression_model_iris_230425.pkl","wb")
joblib.dump(model, model_file)
model_file.close()