# -*- coding:utf-8 -*-
import streamlit as st
import pingouin as pg
import numpy as np

def run_stat_app():
    st.title(pg.__version__)
    np.random.seed(123)

    st.title('T-Test Test')
    N = int(st.number_input("N-Size 입력", value = 30))
    mean, cov, n = [4, 5], [(1, .6), (.6, 1)], N
    x, y = np.random.multivariate_normal(mean, cov, n).T

    # T-test
    result = pg.ttest(x, y)
    st.dataframe(result)