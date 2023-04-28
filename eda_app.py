# -*- coding:utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils

def run_eda_app():
    st.subheader("탐색적 자료 분석")

    iris = pd.read_csv('data/iris.csv')
    st.markdown('## IRIS 확인')
    st.write(iris)   # 대시보드로 나오므로 print 필요없음.

    # 메뉴 지정
    submenu = st.sidebar.selectbox('하위메뉴', ['기술통계량', '그래프분석', '통계분석'])
    if submenu == '기술통계량':
        st.dataframe(iris)

        with st.expander('데이터 타입'):           # expander 숨겨졌다가 보여지게 만들어줌
            result1 = pd.DataFrame(iris.dtypes)
            st.write(result1)
        with st.expander('기술 통계량'):
            result2 = iris.describe()
            st.write(result2)
        with st.expander("타깃 빈도 수 확인"):
            st.write(iris['species'].value_counts())

    elif submenu == '그래프분석':
        st.title("Title")

        with st.expander('산점도'):
            fig1 = px.scatter(iris, x='sepal_width', y='sepal_length', color='species', size='petal_width',
                             hover_data=['petal_length'])
            st.plotly_chart(fig1)

        # layouts
        col1, col2 , col3 = st.columns(3)
        with col1:
            st.title('Seaborn')
            # 그래프 작성
            fig2, ax =plt.subplots()
            sns.boxplot(iris, x='sepal_width', y='sepal_length')
            st.pyplot(fig2)

        with col2:
            st.title('Matplotlib_boxplot')
            # 그래프 작성
            fig3, ax = plt.subplots()
            ax.boxplot(iris['petal_width'])
            st.pyplot(fig3)

        with col3:
            #st.title("Matplotlib_hist")
            fig4, ax =plt.subplots()
            ax.hist(iris['sepal_length'], color='pink')
            st.pyplot(fig4)

            #Tabs
        tab1, tab2, tab3 = st.tabs(['탭1', '탭2', '탭3'])
        with tab1:
            st.write('뭐야')
             # 종 선택할 때마다 산점도 그래프가 달라지도록 함.

            choice = st.selectbox('종 선택', iris['species'].unique())
            result = iris[iris['species'] == choice].reset_index(drop=True)

            col1, col2 = st.columns([0.5,0.5], gap='large')
            with col1:
                # fig5, ax = plt.subplots()
                fig1 = px.scatter(result, x='petal_length', y='sepal_width')
                st.plotly_chart(fig1)

            with col2:
                # fig6, ax = plt.subplots()
                fig2 = px.scatter(result, x='sepal_length', y='sepal_width')
                st.plotly_chart(fig2)

        with tab2:
            st.write('신기해')
            # 캐글 데이터 해당 데이터 그래프 1개만 그려보기
            clinical = pd.read_csv('data/train_clinical_data.csv')
            st.dataframe(clinical, 500, 100)
            updrs = clinical['updrs_1',  'updrs_2', 'updrs_3', 'updrs_4']
            clinical['quarter'] = clinical['visit_month']//3
            #mean =
            choice = st.selectbox('updrs', updrs)
            result = updrs[updrs['updrs'] == choice].reset_index(drop=True)

            col1, col2 = st.columns([0.5,0.5], gap='large')
            with col1:
                #fig, ax = plt.subplots()
                fig1=px.line(result, x='updrs', y=clinical['quarter'])
                st.plotly_chart(fig1)



    elif submenu == '통계분석':
        pass
    else:
        st.warning("뭔가 없어요!")
