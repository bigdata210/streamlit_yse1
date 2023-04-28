# -*- coding:utf-8 -*-
import streamlit as st
import joblib
import os
import numpy as np

def run_ml_app():
    st.title("머신러닝 페이지")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("수치를 입력해주세요!")
        sepal_length = st.select_slider("Sepal Length", options =np.arange(1, 11))
        sepal_width = st.select_slider("Sepal Width", options=np.arange(1, 11))
        petal_length = st.select_slider("Petal Length", options=np.arange(1, 11))
        petal_width = st.select_slider("Petal Width", options=np.arange(1, 11))

        sample = [sepal_length, sepal_width, petal_length, petal_width]
        st.write(sample)

    with col2:
        st.subheader("모델 결과를 확인해주세요!")
        # 2차원 형태로 배열을 만들어줌.
        new_df = np.array(sample).reshape(1, -1)
        st.write(new_df.shape, new_df.ndim)
        MODEL_PATH = 'models/logistic_regression_model_iris_230425.pkl'
        model = joblib.load(open(os.path.join(MODEL_PATH), 'rb'))
        prediction = model.predict(new_df)
        st.write(prediction)

        pred_prob = model.predict_proba(new_df)
        st.write(pred_prob)

    if prediction == 0:
        st.success("Setosa 종입니다. ")
        pred_proba_scores = {"Setosa 확률": pred_prob[0][0] * 100,
                             "Versicolor 확률": pred_prob[0][1] * 100,
                             "Virginica 확률": pred_prob[0][2] * 100}
        st.write(pred_proba_scores)
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Irissetosa1.jpg/220px-Irissetosa1.jpg')

    elif prediction == 1:
        st.success("Versicolor 종입니다.")
        pred_proba_scores = {"Setosa 확률": pred_prob[0][0] * 100,
                             "Versicolor 확률": pred_prob[0][1] * 100,
                             "Virginica 확률": pred_prob[0][2] * 100}
        st.write(pred_proba_scores)
        st.image(
            'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Blue_Flag%2C_Ottawa.jpg/220px-Blue_Flag%2C_Ottawa.jpg')

    elif prediction == 2:
        st.success("Virginica 종입니다.")
        pred_proba_scores = {"Setosa 확률": pred_prob[0][0] * 100,
                             "Versicolor 확률": pred_prob[0][1] * 100,
                             "Virginica 확률": pred_prob[0][2] * 100}
        st.write(pred_proba_scores)
        st.image(
            'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/220px-Iris_virginica_2.jpg')
    else:
        st.warning("판별 불가")